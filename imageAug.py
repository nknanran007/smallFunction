import cv2
import imutils
import numpy as np


#===============================RGB空间的图像对比度/亮度调节
def contrast_and_brightness(img):
    ''''''
    cnum = 1#通常在(1,20)范围
    bnum = 0#通常在(0,100)范围
    cimg = np.ones((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    eles1 = 0.1 * cnum * img[:,:,0] + bnum
    eles2 = 0.1 * cnum * img[:,:,1] + bnum
    eles3 = 0.1 * cnum * img[:,:,2] + bnum
    cimg[:,:,0] = eles1
    cimg[:,:,1] = eles2
    cimg[:,:,2] = eles3
    cimg[:,:,0][eles1 > 255] = 255
    cimg[:,:,1][eles2 > 255] = 255
    cimg[:,:,2][eles3 > 255] = 255
    cv2.namedWindow("contrast_and_brightness")
    cv2.imshow("contrast_and_brightness", cimg)
    if cv2.waitKey(0) == 27:
        cv2.destroyAllWindows()


#===============================因为RGB空间对饱和度调节不直观，所以对于饱和度的调节，首先读取图像的像素RGB值然后再转换到HSL空间得到饱和度与亮度值，调整以后再从HSL空间转换到RGB空间的RGB值，完成图像饱和度调整
def saturation_and_lightness(img, hlsImg):
    l, s, MAX_VALUE = 50, 50, 100
    lsImg = np.zeros(img.shape, np.float32)
    hlsCopy = np.copy(hlsImg)
    #1.调整亮度饱和度(线性变换)、 2.将hlsCopy[:,:,1]和hlsCopy[:,:,2]中大于1的全部截取
    hlsCopy[:, :, 1] = (1.0 + l / float(MAX_VALUE)) * hlsCopy[:, :, 1]
    hlsCopy[:, :, 1][hlsCopy[:, :, 1] > 1] = 1
    #HLS空间通道2是饱和度，对饱和度进行线性变换，且最大值在255以内，这一归一化了，所以应在1以内
    hlsCopy[:, :, 2] = (1.0 + s / float(MAX_VALUE)) * hlsCopy[:, :, 2]
    hlsCopy[:, :, 2][hlsCopy[:, :, 2] > 1] = 1
    # HLS2BGR
    lsImg = cv2.cvtColor(hlsCopy, cv2.COLOR_HLS2BGR)
    # 显示调整后的效果
    cv2.namedWindow("l and s", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("l and s", imutils.resize(lsImg, 650))
    if cv2.waitKey(0) == 27:
        cv2.destroyAllWindows()
    


if __name__ == '__main__':
    img = cv2.imread("/home/rannan/TestFactory/SCP/rawImg/5440.png")
    #===>RGB_cbAug
    '''contrast_and_brightness(img)'''
    #<===
    #===>HSL_slAug
    '''fImg = img.astype(np.float32)
    fImg /= 255.0# 图像归一化，且转换为浮点型, 颜色空间转换 BGR转为HLS
    hlsImg = cv2.cvtColor(fImg, cv2.COLOR_BGR2HLS)# HLS空间，三个通道分别是: Hue色相(0)、lightness亮度(1)、saturation饱和度(2)
    saturation_and_lightness(img, hlsImg)'''
    #<===
    #===>sharpAug
    from PIL import Image
    from PIL import ImageEnhance
    image = Image.open('/home/rannan/TestFactory/SCP/rawImg/5440.png')
    #image.show()
    enh_sha = ImageEnhance.Sharpness(image)
    sharpness = 5.0
    image_sharped = enh_sha.enhance(sharpness)
    image_sharped.show()
    #img = Image.open(filepath)
    img_convert_ndarray = np.array(image)#ndarray和image的相互转换
    print("shape:",img_convert_ndarray.shape)
    #ndarray_convert_img= Image.fromarray(img_convert_ndarray )
    #<===



#-------------------------------------------------------------参考-------------------------------------------------------------
#1.【数字图像处理系列二】亮度、对比度、饱和度、锐化、分辨率:https://zhuanlan.zhihu.com/p/44813768
#2.【python图像处理】图像的增强（ImageEnhance类详解）:https://blog.csdn.net/guduruyu/article/details/71124837
