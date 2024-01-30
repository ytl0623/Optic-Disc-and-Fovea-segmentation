import cv2
import os
import numpy as np

img = cv2.imread("/home/ytl0623/data/MI_proj2/data/OD/train/resize_imgs/drishtiGS_001.png")

print(img.shape)
print(np.unique(img))

img2 = cv2.imread("/home/ytl0623/data/MI_proj2/data/OD/train/resize_masks/drishtiGS_001_mask.png")

print(img2.shape)
print(np.unique(img2))
