import cv2 # for image processing
import os # for delete files
import numpy # for arrays

if os.path.isfile('peopleWalking.mp4'):
   peopleWalkingVideo = cv2.VideoCapture('peopleWalking.mp4')
else:
   print("Cannot find video file exiting....")
   exit()

for file in os.listdir(os.getcwd()):
   if file.endswith(".jpg"):
      os.remove(file)

success,image = peopleWalkingVideo.read()
imageArray = []
count = 0
for count in range(60):  # read first 60 frames
  grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  height, width, layers = image.shape
  imageArray.append(grey)
  #cv2.imwrite("frame%d.jpg" % count, grey)     # save frame as JPEG file      
  success,image = peopleWalkingVideo.read()
  

print("Number of frames: {}".format(count + 1))


differenceArray = []
count = 0
for count in range(59): # calculates difference in frames
  differenceArray.append((imageArray[count+1]-imageArray[count]))
  print("Calculating Diffference in frame:")
  print(count)

#cv2.imwrite("TEST.jpg", imageArray[1]-imageArray[0])

print("Length of difference array:")
print(len(differenceArray))

#performs thresholding
dvsFrames = differenceArray

averageValue = numpy.mean(dvsFrames)
print("Mean value is:")
print(averageValue)

for frameNumber in range(len(dvsFrames)):
   print("Frame number:")
   print(frameNumber)
   for pixelNumber in dvsFrames[frameNumber]:
      for pixel in pixelNumber:
         if pixel > (averageValue * 6):
            pixel = 255
         else:
            pixel = 0




size = (width, height)


for x in range(58):
   print("saving frame:")
   print(x)
   cv2.imwrite("frame%d.jpg" % x, differenceArray[x])

#out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

#for i in range(len(dvsFrames)):
#    out.write(dvsFrames[i])
#out.release()



