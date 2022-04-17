import cv2
import numpy as np
import time
import functools


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print("{} ms used".format(round(end - start, 5)))
        return res

    return wrapper


def get_round_mask(img: np.ndarray, center: tuple, radius):
    mask = np.zeros(img.shape[:2], dtype=np.uint8)
    mask = cv2.circle(mask, center, radius, 255, -1)
    return mask


@timer
def test_mask(img: np.ndarray, mask: np.ndarray):
    if img.shape[:2] != mask.shape:
        raise Exception("height/width of input iamge and mask should be the same!")

    h, w, c = img.shape
    img_copy = img.copy()
    for i in range(h):
        for j in range(w):
            if mask[i, j] == 0:
                img_copy[i, j, :] = 0

    return img_copy


@timer
def test_mask2(img: np.ndarray, mask: np.ndarray):
    if img.shape[:2] != mask.shape:
        raise Exception("height/width of input iamge and mask should be the same!")

    dst = cv2.bitwise_and(img, img, mask=mask)

    return dst

@timer
def test_mask3(img: np.ndarray, mask: np.ndarray):
    if img.shape[:2] != mask.shape:
        raise Exception("height/width of input iamge and mask should be the same!")

    norm_mask = mask/255.0
    norm_mask = norm_mask[...,np.newaxis]
    img_copy = img.copy()
    img_copy = (img_copy*norm_mask).astype(np.uint8)

    return img_copy

if __name__ == "__main__":
    img_path = "../images/cat.jpg"
    img = cv2.imread(img_path)
    h, w, c = img.shape
    center = (int(w / 2), int(h / 2))
    radius = int(min(w, h) / 3)
    mask = get_round_mask(img, center, radius)
    cv2.imshow("mask", mask)
    cv2.waitKey(0)

    roi = test_mask(img, mask)
    cv2.imshow("roi", roi)
    cv2.waitKey(0)

    roi2 = test_mask2(img, mask)
    cv2.imshow("roi2", roi2)
    cv2.waitKey(0)

    roi3 = test_mask3(img, mask)
    cv2.imshow("roi3", roi3)
    cv2.waitKey(0)
