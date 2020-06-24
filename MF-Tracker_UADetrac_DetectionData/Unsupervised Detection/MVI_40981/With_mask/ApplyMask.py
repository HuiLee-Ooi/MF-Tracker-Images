import cv2
import numpy as np
import os, sys

Mask = cv2.imread('Mask.png')

path = './PAWCS/'
files = os.listdir( path )
#Image = cv2.imread(path+files[0])

#cv2.imshow('Image', Image)
#cv2.imshow('Mask', Mask)
#cv2.waitKey()
#dst = cv2.bitwise_and(Mask, Image)
#cv2.imshow('with Mask', dst)
#cv2.waitKey()

for elem in files:
	print('processing...')
	print(path+elem)
	Image =cv2.imread(path+elem)
	if Image is None:
		continue
	dst = cv2.bitwise_and(Mask, Image)
	cv2.imwrite(path+elem, dst)


path = './PAWCSImot/'
files = os.listdir( path )
#Image = cv2.imread(path+files[0])

#cv2.imshow('Image', Image)
#cv2.imshow('Mask', Mask)
#cv2.waitKey()
#dst = cv2.bitwise_and(Mask, Image)
#cv2.imshow('with Mask', dst)
#cv2.waitKey()

for elem in files:
	print('processing...')
	print(path+elem)
	Image =cv2.imread(path+elem)
	if Image is None:
		continue
	dst = cv2.bitwise_and(Mask, Image)
	cv2.imwrite(path+elem, dst)

path = './ViBe/'
files = os.listdir( path )
#Image = cv2.imread(path+files[0])

#cv2.imshow('Image', Image)
#cv2.imshow('Mask', Mask)
#cv2.waitKey()
#dst = cv2.bitwise_and(Mask, Image)
#cv2.imshow('with Mask', dst)
#cv2.waitKey()

for elem in files:
	print('processing...')
	print(path+elem)
	Image =cv2.imread(path+elem)
	if Image is None:
		continue	
	dst = cv2.bitwise_and(Mask, Image)
	cv2.imwrite(path+elem, dst)

path = './ViBeImot/'
files = os.listdir( path )
#Image = cv2.imread(path+files[0])

#cv2.imshow('Image', Image)
#cv2.imshow('Mask', Mask)
#cv2.waitKey()
#dst = cv2.bitwise_and(Mask, Image)
#cv2.imshow('with Mask', dst)
#cv2.waitKey()

for elem in files:
	print('processing...')
	print(path+elem)
	Image =cv2.imread(path+elem)
	if Image is None:
		continue	
	dst = cv2.bitwise_and(Mask, Image)
	cv2.imwrite(path+elem, dst)
