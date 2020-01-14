import sys
import os
import cv2

if len(sys.argv) == 1:
    print("No input file specified. Please specify a video file. Exiting....");
    exit();

videoFileName = sys.argv[1]
folderName = videoFileName.split('.')
folderName = folderName[0]

if os.path.isfile(videoFileName):
   videoFile = cv2.VideoCapture(videoFileName)
else:
   print("Cannot find video file. Exiting....")
   exit()
   

success,image = videoFile.read()
imageArray = []
frameCount = 0
 
if not os.path.isdir(folderName):
  os.mkdir(folderName) 


while success:
  frameCount = int(frameCount) + 1
  frameCount = format(frameCount, "04"); 
  print(frameCount)
  #grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  height, width, layers = image.shape
  imageArray.append(image)
  cv2.imwrite("%s/%sframe.jpg" % (folderName, frameCount), image)     # save frame as JPEG file      
  success,image = videoFile.read()
  
  