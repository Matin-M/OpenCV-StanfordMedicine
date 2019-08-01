import cv2
import sys
from matplotlib import pyplot as plt
import numpy as np
#import ctypes

#def Mbox(title, text, style):
#  return cytypes.windll.user32.MessageBox32.MessageBoxW(0, text, title, style)

#Mbox("vars","input",1)

# read original image
filename = "01039201201150505544528.jpg"

print("Filename and threshold value noted.  ")
#image input. 
image = cv2.imread(filename)


def histogram(filename):
    processImage = cv2.imread(filename = filename, flags = cv2.IMREAD_GRAYSCALE)

    #histogram is a one dimensional numpy array. 
    histogram = cv2.calcHist(images = [processImage], channels = [0], mask = None, histSize = [256], ranges = [0,256])
    
    # configure and draw the histogram figure
    plt.figure()
    plt.title("Greyscale Histogram Analysis")
    plt.xlabel("Pixel Value")
    plt.ylabel("Pixels")
    plt.xlim([0, 256]) # <- named arguments do not work here

    plt.plot(histogram) # <- or here
    plt.show()

    #return histogram
    return histogram

def histogramAnalysis(histogram):
    #maxVal = np.amax(histogram)
    newList = histogram.tolist()
    max_pixel_density = 256
    max__pixel_value = 0
    for (i, c) in enumerate(contour_array):
        print(i)
        print (len(c))
   

    
#calling the histogram function
histogram(filename)
#print(histogramAnalysis(histogram(filename)))
# create binary image
# create binary image

#The pixels of value t will be turned 'off'
#Fixed level thresholding
t = int(input("Enter threshold value"))

def find_contours(binary):
    #return second parameter in tuple, ignore rest of returnVals.
    contours, _ = cv2.findContours(image = binary, mode = cv2.RETR_EXTERNAL, method = cv2.CHAIN_APPROX_SIMPLE)
    print("The countour is a {}".format(type(contours)))
    return contours

#Thresholding and image processing. 
gray = cv2.cvtColor(src = image, code = cv2.COLOR_BGR2GRAY)
#Blur application
blur = cv2.GaussianBlur(src = gray, ksize = (5, 5), sigmaX = 0)
#resultant Binary image. 
(t, binary) = cv2.threshold(src = blur, thresh = t, maxval = 255, type = cv2.THRESH_BINARY_INV)

contour_array = find_contours(binary)

print(contour_array)

print("Found %d objects." % len(contour_array))
for (i, c) in enumerate(contour_array):
    print("\tSize of contour %d: %d" % (i, len(c)))

cv2.drawContours(image, contour_array, contourIdx = -1, color = (0, 255, 0), thickness = 3)

cv2.imshow("binary: ", binary)
cv2.imshow("contours: ", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


