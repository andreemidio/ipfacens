import cv2
import imutils
import numpy as np


imagem = 'placa.png'

img = cv2.imread(imagem, cv2.IMREAD_COLOR)
img = cv2.resize(img, (600, 400))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 13, 15, 15)

edged = cv2.Canny(gray, 30, 200)
contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
screenCnt = None

for c in contours:

    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.018 * peri, True)

    if len(approx) == 4:
        screenCnt = approx
        break

if screenCnt is None:
    detected = 0
    print("No contour detected")
else:
    detected = 1

if detected == 1:
    cv2.drawContours(img, [screenCnt], -1, (0, 0, 255), 3)

mask = np.zeros(gray.shape, np.uint8)
new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1, )
new_image = cv2.bitwise_and(img, img, mask=mask)

(x, y) = np.where(mask == 255)
(topx, topy) = (np.min(x), np.min(y))
(bottomx, bottomy) = (np.max(x), np.max(y))
Cropped = gray[topx:bottomx + 1, topy:bottomy + 1]



print("programming_fever's License Plate Recognition\n")
print("Detected license plate Number is:")
img = cv2.resize(img, (500, 300))
Cropped = cv2.resize(Cropped, (400, 200))
cv2.imshow('car', img)
cv2.imshow('Cropped', Cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()



# contours = imutils.grab_contours(contours)
# contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
# screenCnt = None

_, mask = cv2.threshold(grey, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

document_contour = list()

face_cascade = cv2.CascadeClassifier()
face_cascade.load('haarcascade_licence_plate_rus_16stages.xml')

frame_gray = cv2.equalizeHist(grey)
# -- Detect faces


faces = face_cascade.detectMultiScale(frame_gray, 1.2)

for (x, y, w, h) in faces:
    faceROI = frame_gray[y:y + h, x:x + w]

    cv2.imwrite('result.jpg', faceROI)

for contour in contours:
    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.018 * peri, True)

    if len(approx) == 4:
        screenCnt = approx
        document_contour.append([approx])
        cv2.drawContours(imagem, [approx], -1, (0, 255, 0), 2)
        break

print(len(document_contour))