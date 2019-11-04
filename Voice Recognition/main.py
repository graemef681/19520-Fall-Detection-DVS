# A basic speech recognition program

import speech_recognition as sr
import pocketsphinx as ps
import os

directory_in_str = "./Dataset/yes/" #define directory of files to recognise
recog = sr.Recognizer() #create a reconiser

directory = os.fsencode(directory_in_str)
#print(directory)
count=0
count2 = 0
num = 1
for file in os.listdir(directory):
     filename = os.fsdecode(file)
     if filename.endswith(".wav"):
        yes = sr.AudioFile(directory_in_str+filename)
        with yes as source:
            audio = recog.record(source) #pull in audio signal from file
     try:
        result = recog.recognize_sphinx(audio)
        print(result)  # use pocketsphinx to recognise the speech
        if (result == "yes" or result=="yeah"):
            count = count + 1
        else:
            print(result, ": ", num)
     except: #if it can't tell what it is it throws an exception, so catch it
        print("No transcription available for " + filename)
        count2= count2+1
     print(num) #how far through are we
     num=num +1

print("final count = ")
print(count)
print("no transcript")
print(count2)
