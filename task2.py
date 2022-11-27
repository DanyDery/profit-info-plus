import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="path to the image file")
ap.add_argument("-r", "--radius", type=int,
                help="radius of Gaussian blur; must be odd")
args = vars(ap.parse_args())

# load the image and convert it to grayscale
image = cv2.imread(args["image"])
orig = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# apply a Gaussian blur to the image then find the brightest region
gray = cv2.GaussianBlur(gray, (args["radius"], args["radius"]), 0)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
image = orig.copy()
cv2.circle(image, maxLoc, args["radius"], (255, 0, 0), 2)
cv2.circle(image, minLoc, args["radius"], (0, 255, 0), 2)

# display the results, where green circle - darkness area, blue - brightest
cv2.imshow("solution", image)
cv2.waitKey(0)

#  python task2.py --image mammografia-snimok.jpg --radius 41
