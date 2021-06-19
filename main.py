import cv2
import imutils
import numpy as np

img = 'placa.png'

imagem = cv2.imread(img)

grey = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

blur = cv2.GaussianBlur(hsv, (5, 5), 0)

kernel = np.ones((5, 5), np.uint8)

dilate = cv2.dilate(blur, kernel, iterations=7)

ret, thresh = cv2.threshold(dilate, 170, 255, 0)

graybilateralFilter = cv2.bilateralFilter(grey, 10, 15, 15)

canny = cv2.Canny(thresh, 10, 75)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# cv2.imshow('Imagem', canny)
# cv2.imshow('hsv', hsv)
# cv2.imshow('dilate', dilate)
# cv2.imshow('thresh', thresh)
# cv2.imshow('mask_inv', mask_inv)
cv2.imshow('imagem', imagem)
# cv2.imshow('canny', canny)
cv2.imshow('blur', blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
exit()


"""
filtros morfológicos
canny
"""