# A basic speech recognition program from microphone
# Kirsty Purden
#Last Edited 21/02/20
#--------------------------------------------------------------------------------
#--------------------------------Library imports--------------------------------
import os
from RecordSpeech import *
from TextToSpeech import *
from voiceRecog import *
from setup import *
from makeCall import *

#--------------------------------Global Variable --------------------------------
noTries = 0 #number of tries to get clear answer from user
qNo = 1 #which file to play
haveDetails = True
finished =0 #have we done what we need to

#-------------------------------First time setup---------------------------------
if(haveDetails is True):#(take in the contact details, make the tts files)
    print('Loading previous contact details')
    name, phonenumber = importDetails()
else: # load the existing details
    name, phonenumber = getDetails()

while finished==0: # until we have reached a conclusion
    #-----------------------------Speak to the user-----------------------------
    speak("q", qNo) #text to speec test function

    #---------------------------Record their response---------------------------
    outputpath = "./output.wav"
    audio_filename = record_input(outputpath)

    #-------------------Alternatively, type response (for testing)------------
    '''
    print("Please enter the srGuess:")
    srGuess = str(input())
    '''

    #----------------------Recognise Speech-----------------------------------
    inputpath = './output.wav'
    srGuess = basic(inputpath)

    #-------------------------check category of answer-----------------------
     #i.e. check for things like yeah, nah etc.
     #change guess based on that
    if "yeah" in srGuess or  "yah" in srGuess or srGuess == "eye" or srGuess =="I do" or "yes" in srGuess or srGuess.startswith("ye"): #since I assume it won't know aye
        print("sr guess ", srGuess, " has been changed to yes")
        srGuess = "yes"
    elif srGuess =="nah" or "nah" in srGuess or srGuess == "naw" or "naw" in srGuess or srGuess == "I don't" or "no" in srGuess or srGuess.startswith("n"):
        print("fsr guess ", srGuess, " has been changed to no")
        srGuess = "no"
    elif "stop" in srGuess or srGuess.startswith("st") or srGuess.endswith("op") or srGuess == "hop":
        srGuess = "stop"

    #-------------------------Confirm Answer/Make Decision--------------------
    if srGuess =="yes":
        print("Yes")
        if qNo==1:
            #call the appropriate person
            phoneEmergencyServices()
            speak("r", qNo) #tell the user you've called who it needs
            finished = 1  # once we've called that's us done
        elif qNo ==2:
            # call the appropriate person
            phoneFriend(phonenumber)
            speak("r", qNo)  # tell the user you've called who it needs
            finished = 1  # once we've called that's us done
        else:
              #we're at q3 and the user still needs help
            finished=0#keep going
            qNo = 1 #back to first q
            noTries = noTries+1 # don't want to keep looping forever, at some point got to call ambulance if we can't tell what help they need
    elif srGuess =="no":
          print("No")
          #do action based on answer no
          finished = 0 #we need to keep going
          if qNo==3: #if we'e asked all the questions and the answer is still no
               #the user does not need help
               speak("r",3)
               finished =1
          else:
               #move onto next question
               qNo = qNo+1
               finished =0
    elif srGuess == "stop" : #if the user tells the system to stop
        # the user does not need help
        speak("r", 3)
        finished = 1
    elif srGuess == "Can't recognise speech" and noTries<3:
          print("Can't recognise speech")
          #ask the user again (so keep qNo as it is)
          speak("r",4)
          finished =0
          noTries = noTries +1
    elif noTries>=3:
           print("Out of tries")
           speak("r",1) #user not giving clear replies so call ambulance
           phoneEmergencyServices()
           finished =1 #now we've called help we're done
    else:
        print("Other case: srGuess = ", srGuess)
        #no answer or answers disagree
        #ask user again
        speak("r", 4) #sorry i didn't hear that
        #keep qNo the same
        finished =0 #need to keep going
        noTries = noTries+1 #increment noTries

print ('we have reached the end')

