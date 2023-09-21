# a program to read an image and dislay it patch and transposed patch
# uncomment the program to run
'''
import cv2

img = cv2.imread('zidane.jpg')                      # enter the image here
cv2.imshow('zidane', img)
cv2.waitKey(0)

cv2.namedWindow('zidane_p', cv2.WINDOW_NORMAL)
cv2.namedWindow('zidane_t',cv2.WINDOW_NORMAL)
for i in range (0, img.shape[0]-500, 10):           # (0 is the starting pixel, img.shape[0]-500 is the total no. of pixels, 10 is the step size)
    for j in range(0, img.shape[1]-500, 10):
        patch = img[i:i+500, j:j+500]
        cv2.imshow('zidane_p', patch)
        cv2.waitKey(50)            
        patch02 = cv2.transpose(patch)
        patch02 = cv2.flip(patch02, flipCode=1)                   
        cv2.imshow('zidane_t', patch02)
        cv2.waitKey(50)

cv2.destroyAllWindows()
'''
# --------------------------------------------------------------------

# a sliding window program for while loop
# uncomment the program to run
'''
import cv2

img = cv2.imread('zidane.jpg')                      # enter your image here
cv2.imshow('zidane', img)
cv2.waitKey(0)

i=0
while i<img.shape[0]-500:
  j=0
  while j<img.shape[1]-500:
    patch = img[i:i+500, j:j+500]    
    j+=25                                           # change the step size here
    cv2.imshow('patch',patch)
    cv2.waitKey(5)
  i+=25                                             # change the step size here

cv2.destroyAllWindows()
'''