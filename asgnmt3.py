import numpy as np
import cv2
b = np.zeros([640,640],dtype = 'uint8')
for j in range(80,640,160):
        for i in range (80,640,160):   
            b[j-80:j,i-80:i] = 255
            b[j:j+80,i:i+80] = 255 
cv2.imshow('checker board 8*8',b)
cv2.waitKey(0)
cv2.destroyAllWindows()
