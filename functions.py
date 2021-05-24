import cv2 as cv
import numpy as np
import imutils


# ****** Görüntü Açmak *********#
def görüntüAl():
    img = cv.imread('sahibinden.jpg')
    return img


# ****** Griye Çevirme *********#
def griyeCevir():
    img = görüntüAl()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return gray


# ****** Bileteral Filtre Uygulama *********#
def bileteralFiltre():
    gray = griyeCevir()
    bileteral = cv.bilateralFilter(gray, 11, 17, 17)
    return bileteral


# ****** Canny Edge Almak *********#
def cannyEdgeAl():
    bileteral = bileteralFiltre()
    cannyEdge = cv.Canny(bileteral, 30, 200)
    return cannyEdge


# ****** Kontur Almak, Plaka Yeri Tespiti, Plakanın Tespiti ve Maskelenmesi *********#
def konturAlKırp():
    img = görüntüAl()
    gray = griyeCevir()
    cannyEdge = cannyEdgeAl()
    keyPoints = cv.findContours(cannyEdge, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keyPoints)
    contours = sorted(contours, key=cv.contourArea, reverse=True)[:10]
    location = None
    for contour in contours:
        approx = cv.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            location = approx
            break
    mask = np.zeros(gray.shape, np.uint8)
    new_image = cv.drawContours(mask, [location], 0, 255, -1)
    new_image = cv.bitwise_and(img, img, mask=mask)
    (x, y) = np.where(mask == 255)
    (x1, y1) = (np.min(x), np.min(y))
    (x2, y2) = (np.max(x), np.max(y))
    cropper_image = gray[x1:x2 + 1, y1:y2 + 1]
    return cropper_image
