import numpy as np


def nms(bboxes:np.ndarray, scores:np.ndarray, labels:np.ndarray, threshold):
    suppressed = np.zeros(scores.shape[0], dtype=np.bool)
    x1 = np.ascontiguousarray(bboxes[:, 0])
    y1 = np.ascontiguousarray(bboxes[:, 1])
    x2 = np.ascontiguousarray(bboxes[:, 2])
    y2 = np.ascontiguousarray(bboxes[:, 3])

    order_indices = np.argsort(-scores)
    ndets = scores.shape[0]
    
    for i in range(ndets):
        index = order_indices[i]
        
        if suppressed[index]:
            continue
        
        label = labels[index]
        x1_i = x1[index]
        y1_i = y1[index]
        x2_i = x2[index]
        y2_i = y2[index]
        area_i = (y2_i - y1_i) * (x2_i - x1_i) 
        for j in range(i, ndets):
            index_j = order_indices[j]
            if suppressed[index_j]:
                continue

            label_j = labels[index_j]
            if label_j != label:
                continue

            
            x1_j = x1[index_j]
            y1_j = y1[index_j]
            x2_j = x2[index_j]
            y2_j = y2[index_j]

            xx1 = max(x1_i, x1_j)
            yy1 = max(y1_i, y1_j)
            xx2 = min(x2_i, x2_j)
            yy2 = max(y2_i, y2_j)

            area_j = (x2_j - x1_j) * (y2_j - y1_j)

            inter = (xx2 - xx1) * (yy2 - yy1)
            iou = inter / (area_i + area_j - inter)

            if iou > threshold:
                suppressed[index_j] = True
    
    return ~suppressed

def nms_parrallel(bboxes:np.ndarray, scores:np.ndarray, nms_threshold:float):
    sorted_inds = np.argsort(scores)[...-1]
    keep = []
    x1, y1, x2, y2 = bboxes[:, 0], bboxes[:, 1], bboxes[:, 2], bboxes[:, 3]
    area = (x2 - x1 + 1) * (y2 - y1 + 1)

    while len(sorted_inds) > 0:
        index_i = sorted_inds[0]
        keep.append(index_i)

        xx1 = np.maximum(x1[index_i], x1[sorted_inds[1:]])
        yy1 = np.maximum(y1[index_i], y1[sorted_inds[1:]])
        xx2 = np.minimum(x2[index_i], x2[sorted_inds[1:]])
        yy2 = np.minimum(y2[index_i], y2[sorted_inds[1:]])

        union = np.maximum(0, xx2 - xx1 + 1) * np.maximum(0, yy2 - yy1 + 1)
        iou = union / (area[index_i] + area[sorted_inds[1:]] - union)
        inds = iou < nms_threshold
        sorted_inds = sorted_inds[inds+1]
    
    return bboxes[keep]
    
        


            

def conv(input, kernel, stride=1, padding=1):
    '''
    input : (B, C_i, H, W)
    kernel: (C_o, C_i, k_w, k_h)
    output: (B, C_o, H_o, W_o)
    '''
    B, C_i, H, W = input.shape
    C_o, C_i_k, k_h, k_w = kernel.shape
    assert C_i == C_i_k
    H_o = int((H - k_h + 2 * padding)/stride + 1)
    W_o = int((W - k_w + 2 * padding)/stride + 1)
    res = np.zeros((B, C_o, H_o, W_o))

    input_padded = np.pad(input, ((0,0), (0,0), (padding, padding), (padding, padding)), mode='constant')

    for b in range(B):
        for c in range(C_o): 
            for h in range(0, H+2*padding-k_h+stride, stride):
                for w in range(0, W+2*padding-k_w+stride, stride):
                    res[b, c, h//stride, w//stride] = np.sum(input_padded[b, :, h:h+k_h, w:w+k_w] * kernel[c, :, :, :])
    return res

def test():
    input = np.array([[2,3,7,4,6,2,9],
                        [6,6,9,8,7,4,3],
                        [3,4,8,3,8,9,7],
                        [7,8,3,6,6,3,4],
                        [4,2,1,8,3,4,6],
                        [3,2,4,1,9,8,3],
                        [0,1,3,9,2,1,4]]).reshape((1, 1, 7, 7))
    kernel = np.array([[3,4,4],
                        [1,0,2],
                        [-1,0,3]]).reshape(1, 1, 3, 3)
    

    print(conv_img2col(input, kernel, stride=2, padding=0))


def get_indices(input_shape, k_h, k_w, stride, padding):
    b, c, h, w = input_shape

    out_h = int((h - k_h + 2 *padding)/stride + 1)
    out_w = int((w - k_w + 2 *padding)/stride + 1)

    # create y vectors
    level1 = np.repeat(np.arange(k_h), k_w)
    level1 = np.tile(level1, c)
    everylevels = stride * np.repeat(np.arange(out_h), out_w)
    y = level1.reshape(-1, 1) + everylevels.reshape(1, -1)


    # create x vectors
    slide1 = np.tile(np.arange(k_w), k_h)
    slide1 = np.tile(slide1, c)
    everyslides = stride * np.tile(np.arange(out_w), out_h)
    x = slide1.reshape(-1, 1) + everyslides.reshape(1, -1)


    # creata b vetcors
    d = np.repeat(np.arange(c), k_h * k_w).reshape(-1, 1)
    return y, x, d

def img2col(input, k_h, k_w, stride=1, padding=1):
    padded = np.pad(input, ((0,0),(0,0),(padding, padding), (padding, padding)), mode='constant')
    y, x, d = get_indices(input.shape, k_h, k_w, stride, padding)
    cols = padded[:, d, y, x]
    # cols shape (B, c_i*k_w*k_h, h_o*w_o)
    return cols


def conv_img2col(input, kernel, stride=1, padding=1):
    c_o, c_i, k_h, k_w = kernel.shape
    b, _, h, w = input

    out_h = int((h - k_h + 2 *padding)/stride + 1)
    out_w = int((w - k_w + 2 *padding)/stride + 1)
    
    #input col shape (B, c_i*k_w*k_h, h_o*w_o)
    input_col = img2col(input, k_h, k_w, stride, padding)
    # kernel shape (c_o, c_i*k_w*k_h)
    kernel = kernel.reshape(c_o, -1)
    out = []
    for input_ in input_col:
        out.append(kernel @ input_)
    out = np.stack(out, axis=0)
    out = out.reshape((b, c_o, out_h, out_w))
    return out


class BN2d:
    def __init__(self, eps=1e-5, affine=True, track_running_status=True, monentum=0.1):
        self.monentum = monentum
        self.track_running_status = track_running_status
        if self.track_running_status:
            self.running_mean = 0
            self.running_var = 0
        self.eps = eps
        self.affine = affine
        if self.affine:
            self.gamma = np.ones((1,))
            self.beta = np.zeros((1,))
        self.eval = False

    def eval(self):
        self.eval = True

    def forward(self, input):
        if self.eval:
            normalized = input - self.running_mean.reshape(1, -1, 1, 1)/np.sqrt(self.running_var.reshape(1, -1, 1, 1) + self.eps)
            if not self.affine:
                return normalized
            else:
                return normalized * self.gamma.reshape(1, -1, 1, 1) + self.beta.reshape(1, -1, 1,1)
        else:
            B, C, H, W = input.shape
            mean = np.mean(input, axis=(0, 2, 3))
            var = np.var(input, axis=(0, 2, 3))
            normalized = input - mean.reshape(1, -1, 1, 1) / np.sqrt(var.reshape(1, -1, 1, 1) + self.eps)
            if self.track_running_status:
                self.running_mean = self.monentum * self.running_mean + (1-self.monentum) * mean
                self.running_var = self.monentum * self.running_var + (1-self.monentum) * var
            if self.affine:
                normalized = normalized * self.gamma.reshape(1, -1, 1, 1) + self.beta.reshape(1, -1, 1,1)

            return normalized
        

class SigmoidFocalLoss:
    def __init__(self, alpha=0.25, gamma=2):
        self.alpha = alpha
        self.gamma = gamma
    
    def forward(self, x, targets):
        n_class = p.shape[-1]
        p = x.sigmoid()
        term1 = (1-p) ** self.gamma * np.log(p)
        term2 = p ** self.gamma * np.log(1-p)
        class_ids = np.arange(1, n_class+1).reshape(1, -1)
        t = targets.reshape(-1, 1)
        loss = (-(class_ids == targets) * self.alpha * term1) + (-(class_ids != targets)*(1- self.alpha) * term2)
        loss = loss.sum()
        return loss

if __name__ == '__main__':
    bn = BN2d()
    input = np.random.random((3, 3, 240, 240))
    print(bn.forward(input).shape)
                    


