import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype=np.uint8)
pts = [[[100, 100], [300, 150], [300, 350], [250, 450], [50, 450]]]
pts = np.array(pts)
# poly_img = cv2.polylines(canvas, pts, True, (255, 255, 255), 1, 8, 0)
# cv2.imshow("polylines", poly_img)
# cv2.waitKey(0)


filled_poly_img = cv2.fillPoly(canvas, pts, (255, 255, 255), 8, 0)
cv2.imshow("filled poly", filled_poly_img)
cv2.waitKey(0)
