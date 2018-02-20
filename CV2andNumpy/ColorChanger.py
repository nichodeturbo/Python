import cv2
import numpy as np
import time


 
# read image into matrix.
m =  cv2.imread("/Users/nichodeturbo/Desktop/Python_Code/seth.jpg")
 
h,w,bpp = np.shape(m)
 
# iterate over the entire image.
question = input("Would you like to see something neat?\n")

for py in range(0,h):
    for px in range(0,w):
        if question == "y":
            m[py][px][0] = 100
        else:
            m[py][px][1] = 100
       
  
    
 
# display image
cv2.imshow("Seth's Program.", m)
cv2.waitKey(0)
