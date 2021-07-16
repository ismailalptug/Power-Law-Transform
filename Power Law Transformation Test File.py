import cv2
from Power_Law_Transform import powerlawtransform

inimg = cv2.imread("BLOCKS.TIF")
cv2.imshow("Original",inimg)
powerlawtransform(inimg,0.2)