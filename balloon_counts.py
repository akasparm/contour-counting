"""
ENPM673: PERCEPTION FOR AUTONOMOUS ROBOTS
SUBMITTED BY: AKASHKUMAR PARMAR
"""

# Importing required libraries
import numpy as np
import cv2 as cv


def balloons():
        
    bgr_image = cv.imread("hotairbaloon.jpg", 100) # Reading BGR image

    gray_image = cv.cvtColor(bgr_image, cv.COLOR_BGR2GRAY) # Converting the image in gray scale

    blurred_image = cv.GaussianBlur(gray_image, (31, 31), 3) # Blurring the image

    edged_image= cv.Canny(blurred_image, 10, 200) # Applying canny edge detection

    dilated_image = cv.dilate(edged_image, (1, 1), iterations=4) # Dilating the edges to join the intermittent lines

    contours, _ = cv.findContours(dilated_image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE) # Contour detection

    # Iterating through all the contours and collecting the valid contours
    balloons = [] # balloon list
    for i in contours:
        area = cv.contourArea(i) # Area of the contour
        if area > 200: # Area criteria
            balloons.append(i)


    # Putting text on the image with color randomization
    for i in enumerate(balloons):
        if i[0]%2==0:
            cv.putText(bgr_image, str(i[0]+1), tuple(i[1][0][0]-10), cv.FONT_HERSHEY_SIMPLEX, 0.5, tuple([i[0]*16, i[0]*16, i[0]*16]), 2)
        else:
            cv.putText(bgr_image, str(i[0]+1), tuple(i[1][0][0]-10), cv.FONT_HERSHEY_SIMPLEX, 0.5, tuple([255-i[0]*16, 255-i[0]*16, 255-i[0]*2*16]), 2)

    cv.imshow("Question4", bgr_image)
    cv.waitKey(0)
    cv.destroyAllWindows()




def main():
    balloons()


if __name__=="__main__":
    main()