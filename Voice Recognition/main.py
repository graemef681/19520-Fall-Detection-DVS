# A basic speech recognition program from microphone
import os
from RecordSpeech import *
from TextToSpeech import *
from voiceRecog import *
from setup import *
from makeCall import *

noTries = 0 #number of tries to get clear answer from user
qNo = 1 #which file to play
haveDetails = True
finished =0 #have we done what we need to

#------First time setup (take in the contact details, make the tts files)
if(haveDetails is True):
    print('Loading previous contact details')
    importDetails()
else:
    getDetails()

#----------Load Templates--------- Not sure if we need this anymore? Keep for now
temp1, temp2, temp3, temp4 = loadTemplates()

#-------Record the Ambient Noise-------
#outputpath = "./noise.wav"
#noise_filename = record_input(outputpath)


while finished==0: # until we have reached a conclusion
    #-------Speak to the user--------
    speak("q", qNo) #text to speec test function

    #-------Record their response-----
    '''
    outputpath = "./output.wav"
    audio_filename = record_input(outputpath)
    '''

    #-----Alternatively, load a premade response (for filter testing)
    '''
    noise = AudioSegment.from_file("./Household Noise/dog.wav") #cat noise
    input = AudioSegment.from_file(("./Dataset/yes/00f0204f_nohash_0.wav")) # test speech
    signal = signal.overlay(noise)
    signal.export("temp.wav","wav")
    audio_filename = "temp.wav"
    '''

    #-----Alternatively, type response (for decision making testing)
    print("Please enter the srGuess:")
    srGuess = str(input())

    print("Please enter the fsrGuess:")
    fsrGuess = str(input())

    #-----------Filter----------------
    '''
    bandpassed = bandpassSignal(audio_filename)

    #check similarity with yes and no templates
     measure1 = checkSimilarity(bandpassed.get_array_of_samples(),temp1.get_array_of_samples())
     measure2 = checkSimilarity(bandpassed.get_array_of_samples(),temp4.get_array_of_samples())

     if measure1>measure2:
         #then it's yes
         MSEguess = "yes"
         #more correlated with yes template than no so it's probably yes
         filtered = removeNoise(bandpassed,temp1) #check if it's yes
     else:
         MSEguess = "no"
         filtered = removeNoise(bandpassed,temp4) # check if it's no

     #--------guess word from lowest mse comparing to template---------------
     MSEguess = fromMSEGuessWord(filtered)

     #-------Write filtered signal to Output File-------------------
     filename = 'filtered.wav'
     write("./filtered.wav", 16000, np.int16(np.real(filtered)))  # output the file
    '''

    #--------Recognise Speech------------
    '''
     inputpath = 'filtered.wav'
     fsrGuess = basic(inputpath) # recognise the speech

     srGuess = basic("Temp.wav")
     '''

    #----------check category of answer--------
     #i.e. check for things like yeah, nah etc.
     #change guess based on that
    if "yeah" in srGuess or  "yah" in srGuess or srGuess == "eye" or srGuess =="I do" or "yes" in srGuess or srGuess.startswith("ye"): #since I assume it won't know aye
          print("sr guess ", srGuess, " has been changed to yes")
          srGuess = "yes"
    elif srGuess =="nah" or "nah" in srGuess or srGuess == "naw" or "naw" in srGuess or srGuess == "I don't" or "no" in srGuess or srGuess.startswith("n"):
          print("fsr guess ", srGuess, " has been changed to no")
          srGuess = "no"

    if "yeah" in fsrGuess or  "yah" in fsrGuess or fsrGuess == "eye" or fsrGuess =="I do" or "yes" in fsrGuess or fsrGuess.startswith("ye"): #since I assume it won't know aye
          print("fsr guess ", fsrGuess, " has been changed to yes")
          fsrGuess = "yes"
    elif fsrGuess =="nah" or "nah" in fsrGuess or fsrGuess == "naw" or "naw" in fsrGuess or fsrGuess == "I don't" or "no" in fsrGuess or fsrGuess.startswith("N"):
          print("fsr guess ", fsrGuess, " has been changed to no")
          fsrGuess = "no"

    #--------Confirm Answer/Make Decision-------------
    if srGuess =="yes" and fsrGuess == "yes":
        print("Yes")
        if qNo==1:
            #call the appropriate person
            phoneEmergencyServices()
            speak("r", qNo) #tell the user you've called who it needs
            finished = 1  # once we've called that's us done
        elif qNo ==2:
            # call the appropriate person
            phoneFriend()
            speak("r", qNo)  # tell the user you've called who it needs
            finished = 1  # once we've called that's us done
        else:
              #we're at q3 and the user still needs help
            finished=0#keep going
            qNo = 1 #back to first q
            noTries = noTries+1 # don't want to keep looping forever, at some point got to call ambulance if we can't tell what help they need
    elif srGuess =="no" and fsrGuess=="no":
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
        print("Other case: fsrGuess = ", fsrGuess, " and srGuess = ", srGuess)
        #no answer or answers disagree
        #ask user again
        speak("r", 4) #sorry i didn't hear that
        #keep qNo the same
        finished =0 #need to keep going
        noTries = noTries+1 #increment noTries

print ('we have reached the end')

