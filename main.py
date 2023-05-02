import numpy as np
import cv2


def f(x):
    return x


def noise_reduction_sharpening(image):
    kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    new_kernel = (-1) * np.array([[0, 1, 0], [1, -4 - 1, 1], [0, 1, 0]])

    gry_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.namedWindow("Control")
    cv2.createTrackbar("Sigma", "Control", 1, 10, f)
    cv2.createTrackbar("Size", "Control", 1, 10, f)

    while True:
        sigma = cv2.getTrackbarPos("Sigma", "Control")
        size = cv2.getTrackbarPos("Size", "Control")

        if sigma == -1:
            break
        if size % 2 == 0:
            size = size + 1

        blur_img = cv2.GaussianBlur(gry_image, (size, size), sigma)
        result = cv2.filter2D(blur_img, -1, new_kernel)
        cv2.imshow("Result", result)
        key = cv2.waitKey(5)
        if key == 32:
            return result


org = cv2.imread("image.png")
bnw = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)
sharpened = noise_reduction_sharpening(org)

cv2.imshow("sharpened", sharpened)
cv2.waitKey(0)

# Apply binary thresholding
ret, thresh = cv2.threshold(bnw, 170, 255, cv2.THRESH_BINARY_INV)
