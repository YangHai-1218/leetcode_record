import torch
from torch import nn
from torch.nn import functional as F


class BasicBlock(nn.Module):
    def __init__(self, ) -> None:
        super().__init__()
        # no downsamplig
        self.conv1 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1)
        self.relu = nn.ReLU()
        self.conv2 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1)

    def forward(self, x):
        x_ = self.conv1(x)
        x_ = self.relu(x_)
        x_ = self.conv2(x_)
        x_ = self.relu(x_)
        return x_ + x

class BottleneckBlock(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=256, out_channels=64, kernel_size=1, stride=1)
        self.relu = nn.ReLU()
        self.conv2 = nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, stride=1)
        self.conv3 = nn.Conv2d(in_channels=64, out_channels=256, kernel_size=1, stride=1)
    
    def forward(self, x):
        x_ = self.conv1(x)
        x_ = self.relu(x_)
        x_ = self.conv2(x_)
        x_ = self.relu(x_)
        x_ = self.conv3(x_)
        x_ = self.relu(x_)
        return x + x_


# n 分类
# 占比多少？ 估计每一类样本占比
# 算loss，更新类样本占比
class BalancedCELoss(nn.Module):
    def __init__(self, class_num:int) -> None:
        super().__init__()
        self.class_num = class_num
        self.class_distribution = [0. for _ in range(self.class_num)]
        self.step = 0


    def forward(self, pred, tgt):

        # update state dict
        for i in range(self.class_num):
            self.class_distribution[i] = (self.class_distribution[i]*self.step + torch.sum(tgt==i)/tgt.size(0))/(self.step+1)
        self.step += 1
        # compute loss
        # loss = nn.CrossEntropyLoss(weight=)

            


class FocalLoss(nn.Module):
    def __init__(self, alpha=2., gamma=0.25) -> None:
        super().__init__()
        self.alpha = alpha
        self.gamma = gamma
    
    def forward(self, target, pred):
        # target :(N, class_number), pred:(N, class_number)
        # focal_weight = torch.pow((1 - torch.index_select(pred, dim=1, index=target)), self.sigma) # torch.index
        pt = (1 - pred) * target + pred * (1 - target)
        focal_weight = (self.alpha * target + (1 - self.alpha) * (1 - target)) * pt.pow(self.gamma)
        loss = F.binary_cross_entropy(pred, target, reduce='None') * focal_weight
        return loss
    
    # https://garrickbrazil.com/omni3d/