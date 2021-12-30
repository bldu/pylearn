# https://blog.csdn.net/zhangbangqian/article/details/79316994

import cv2
import numpy as np
import math

WINDOW = "test"
drawing = False  # 鼠标左键按下时，该值为True，标记正在绘画
mode = 1  # 1 画矩形，2 画圆, 3 画线
ix, iy = -1, -1  # 鼠标左键按下时的坐标


def draw(event, x, y, flags, param):
    global ix, iy, drawing, mode, img, dynamic_img

    if event == cv2.EVENT_LBUTTONDOWN:
        # 鼠标左键按下事件
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        # 鼠标移动事件
        if drawing == True:
            dynamic_img = img.copy()
            if mode == 1:
                cv2.rectangle(dynamic_img, (ix, iy), (x, y), (0, 255, 0), 1)
            elif mode == 2:
                r = int(math.sqrt((x - ix) ** 2 + (y - iy) ** 2))
                cv2.circle(dynamic_img, (ix, iy), r, (0, 0, 255), 1)
            elif mode == 3:
                cv2.line(dynamic_img, [ix, iy], [x, y], (0, 255, 0), 1)
            # ix, iy = x, y
            cv2.imshow(WINDOW, dynamic_img)

    elif event == cv2.EVENT_LBUTTONUP:
        # 鼠标左键松开事件
        img = dynamic_img.copy()
        drawing = False


if __name__ == "__main__":
    img = np.ones((512, 512, 3), np.uint8)
    img = img * 255
    cv2.imshow(WINDOW, img)

    while 1:
        key = cv2.waitKey(10)
        if key == ord("r"):
            mode = 1
        elif key == ord("o"):
            mode = 2
        elif key == ord("l"):
            mode = 3
        elif key == ord("q"):
            break

        cv2.setMouseCallback(WINDOW, draw)  # 设置鼠标事件的回调函数

    cv2.waitKey(0)
