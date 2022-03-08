# A python implementation of opencv c++ copyTo function.

import cv2

cat_path = "../images/cat.jpg"
dog_path = "../images/dog.jpg"

cat = cv2.imread(cat_path)
dog = cv2.imread(dog_path)

h, w, c = dog.shape

cat = cv2.resize(cat, (int(w / 3), int(h / 3)))

dog[0 : int(h / 3), 0 : int(w / 3)] = cat

cv2.imshow("cat copied to dog", dog)
cv2.waitKey(0)
