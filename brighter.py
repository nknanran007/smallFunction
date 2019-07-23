import cv2
import imutils
import numpy as np

def c_and_b(arg):
    ''''''
    cnum = 15#= cv2.getTrackbarPos(trackbar_name1, wname)
    bnum = 0#= cv2.getTrackbarPos(trackbar_name2, wname)
    #print(bnum)
    cimg = np.ones((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    eles1 = 0.1 * cnum * img[:,:,0] + bnum
    eles2 = 0.1 * cnum * img[:,:,1] + bnum
    eles3 = 0.1 * cnum * img[:,:,2] + bnum
    #print("cimg.shape:",cimg.shape)
    #print("eles.shape:",eles.shape)
    cimg[:,:,0] = eles1
    cimg[:,:,1] = eles2
    cimg[:,:,2] = eles3
    cimg[:,:,0][eles1 > 255] = 255
    cimg[:,:,1][eles2 > 255] = 255
    cimg[:,:,2][eles3 > 255] = 255
    '''for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            lst = 0.1*cnum*img[i, j] + bnum
            cimg[i, j] = [int(ele) if ele < 255 else 255 for ele in lst]'''
    cv2.imshow("c_and_b", cimg)

#wname = 'brightness and contrast'
#trackbar_name1 = 'contrast'
#trackbar_name2 = 'brightness'
img = cv2.imread("./WWL-like5440_2_pure/1049_color.png")
height, width = img.shape[:2]
#img = cv2.resize(img, (int(width/height*400), 400), interpolation=cv2.INTER_CUBIC)

cv2.namedWindow("c_and_b")

#cv2.createTrackbar(trackbar_name1, wname, 10, 20, c_and_b)
#cv2.createTrackbar(trackbar_name2, wname, 0, 100, c_and_b)

c_and_b(0)


if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
