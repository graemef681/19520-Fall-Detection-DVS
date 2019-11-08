import cv2 # for image processing
import os # for delete files
import numpy # for arrays

peopleWalkingVideo = cv2.VideoCapture('peopleWalking.mp4')
success,image = peopleWalkingVideo.read()
imageArray = []
count = 0
for count in range(60):  # read first 60 frames
  grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  imageArray.append(grey)
  #cv2.imwrite("frame%d.jpg" % count, grey)     # save frame as JPEG file      
  success,image = peopleWalkingVideo.read()
  

print("Number of frames: {}".format(count + 1))





for file in os.listdir(os.getcwd()):
   if file.endswith(".jpg"):
      os.remove(file)
