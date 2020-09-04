import cv2 as cv
import operator
import numpy as np
from scipy.spatial import distance
import pytesseract
from matplotlib import pyplot as plt
def pre_process_image(img, skip_dilate=True):
    proc = cv.GaussianBlur(img.copy(), (9, 9), 0)
    proc = cv.adaptiveThreshold(proc, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
    proc = cv.bitwise_not(proc, proc)
    kernel = np.array([[0., 1., 0.], [1., 1., 1.], [0., 1., 0.]],np.uint8)
    proc = cv.dilate(proc, kernel)
    proc=255-proc
    # plt.imshow(proc)
    # plt.show()
    return proc
def distance_between(p1, p2):
	a = p2[0] - p1[0]
	b = p2[1] - p1[1]
	return np.sqrt((a ** 2) + (b ** 2))
def extract_digit(img,rect):
    digit = img[int(rect[0][1]):int(rect[1][1]), int(rect[0][0]):int(rect[1][0])]
    digit = pre_process_image(digit)
    # plt.imshow(digit,cmap='gray')
    # plt.show()

    digit = pytesseract.image_to_string(digit,config='--psm 6')
    if not digit in ['0','1','2','3','4','5','6','7','8','9']:
        digit=0
    return digit
image = cv.imread("D:/python files/SudukoEasy.jpg",0)
image1 = cv.GaussianBlur(image.copy(), (9, 9), 0)
image1 = cv.adaptiveThreshold(image1, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
image1 = cv.bitwise_not(image1, image1)
kernel = np.array([[0., 1., 0.], [1., 1., 1.], [0., 1., 0.]],np.uint8)
image1 = cv.dilate(image1, kernel)
contour,h= cv.findContours(image1.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
contours = sorted(contour, key=cv.contourArea, reverse=True)
polygon = contours[0]

bottom_right, _ = max(enumerate([pt[0][0] + pt[0][1] for pt in
                      polygon]), key=operator.itemgetter(1))
top_left, _ = min(enumerate([pt[0][0] + pt[0][1] for pt in
                  polygon]), key=operator.itemgetter(1))
bottom_left, _ = min(enumerate([pt[0][0] - pt[0][1] for pt in
                     polygon]), key=operator.itemgetter(1))
top_right, _ = max(enumerate([pt[0][0] - pt[0][1] for pt in
                   polygon]), key=operator.itemgetter(1))
top_left=polygon[top_left][0]
top_right=polygon[top_right][0]
bottom_left=polygon[bottom_left][0]
bottom_right = polygon[bottom_right][0]
print(bottom_left)
src = np.array([top_left, top_right, bottom_right, bottom_left], dtype='float32')
side = max([distance_between(bottom_right, top_right),distance_between(top_left, bottom_left),distance_between(bottom_right, bottom_left),distance_between(top_left, top_right) ])
# side = np.array(side,dtype='float32')
dst = np.array([[0, 0], [side - 1, 0], [side - 1, side - 1], [0, side - 1]], dtype='float32')
m = cv.getPerspectiveTransform(src, dst)
cv.warpPerspective(image, m, (int(side), int(side)))
plt.imshow(image)
plt.show()
squares = []
side = image.shape[:1]
side = side[0] / 9
for j in range(9):
    for i in range(9):
        p1 = [i * side+5, j * side]  #Top left corner of a box
        p2 = [(i + 1) * side-5, (j + 1) * side]  #Bottom right corner
        squares.append((p1, p2))
digits = []
# img = pre_process_image(img.copy(), skip_dilate=True)
for square in squares:
    digits.append(int(extract_digit(image, square)))
sudoku=np.reshape(digits, (9, 9))
print(sudoku)
