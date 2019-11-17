# A basic speech recognition program from microphone
from RecordSpeech import *
from TextToSpeech import *
from voiceRecog import *
#from TestFunctions import *

noTries = 0 #number of tries to get clear answer from user

#-------Speak to the user--------
#speak() #text to speec test function

#-------Record their response-----
#outputpath = "./output.wav"
#audio_filename = record_input(outputpath)
audio_filename = "./Dataset/no/0bde966a_nohash_0.wav" #"noisy.wav"

#----------Load Templates---------
template1 = AudioSegment.from_file("./Dataset/Template/0a7c2a8d_nohash_0.wav")  # female yes
template2 = AudioSegment.from_file("./Dataset/Template/0b40aa8e_nohash_0.wav")  # female no
template3 = AudioSegment.from_file("./Dataset/Template/0135f3f2_nohash_0.wav")  # male yes
template4 = AudioSegment.from_file("./Dataset/Template/0b56bcfe_nohash_0.wav")  # male no

#-----------Filter----------------
bandpassed = bandpassSignal(audio_filename)

#check similarity with yes and no templates
measure1 = checkSimilarity(bandpassed.get_array_of_samples(),template1.get_array_of_samples())
measure2 = checkSimilarity(bandpassed.get_array_of_samples(),template4.get_array_of_samples())

if measure1>measure2:
    #more correlated with yes template than no so it's probably yes
    filtered = removeNoise(bandpassed,template1) #check if it's yes
else:
    filtered = removeNoise(bandpassed,template4) # check if it's no

#--------guess word from lowest mse comparing to template---------------
MSEguess = fromMSEGuessWord(filtered)

#-------Write filtered signal to Output File-------------------
filename = 'filtered.wav'
write("filtered.wav", 16000, np.int16(np.real(filtered)))  # output the file

#--------Recognise Speech------------
inputpath = filename
srGuess = basic(inputpath) # recognise the speech

#----------check category of answer--------
#i.e. check for things like yeah, nah etc.
#change guess based on that

#--------Confirm Answer-------------
if srGuess =="yes" and MSEguess == "yes":
    print("Yes")
    #do action based on answer yes
elif srGuess =="no" and MSEguess=="no":
    print("No")
    # do action based on answer no
elif srGuess == "Can't recognise speech" and noTries<3:
    print("Can't recognise speech")
    #ask the user again
    #increment no. tries
elif noTries>=3:
    print("Out of tries")
    #user not giving clear replies so call ambulance
else:
    print("Other case: MSEguess = ", MSEguess, " and srGuess = ", srGuess)
    #no answer or answers disagree
    #ask user again
    #increment noTries

