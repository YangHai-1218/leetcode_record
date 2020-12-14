
import torch
from torch.nn import Conv2d
import time
image = torch.randn((1,3,224,224))
conv2d = Conv2d(in_channels=3, out_channels=32, kernel_size=3)
start = time.perf_counter()
output = conv2d(image)
end = time.perf_counter()
print('Running time: %s Seconds'%(end-start))