import numpy as np
import cv2


def powerlawtransform(img, power):
    newimage = np.array(255*(img/255)**power, dtype='uint8')
    cv2.imshow("PowerLawTransform", newimage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
