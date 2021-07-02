import numpy as np
import os
import cv2

data = np.random.randint(0, high=255, size=(80,80))
print(data)
cv2.imwrite(os.path.join("../images", __file__+".png"), data)