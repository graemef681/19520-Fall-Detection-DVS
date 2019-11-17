from pydub import AudioSegment
from pydub.playback import play
import speech_recognition as sr
from Filtering import bandpassSignal
from voiceRecog import *

import os
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from sklearn.metrics import mean_squared_error

def testRecogWithNoise(): # function to listen to each of the signals combined with noise
    # Load signals
    audio1 = AudioSegment.from_file("./Dataset/no/0b77ee66_nohash_0.wav")
    audio2 = AudioSegment.from_file("./Household Noise/kettle.wav")

    # add noise to signal
    mixed = audio1.overlay(audio2)
    mixed.export("./mixed.wav", format='wav')
    play(mixed) #see what it sounds like to humans

    filtered = bandpassSignal(mixed)
    play(filtered)
    filtered.export("./filtered.wav", format = 'wav')
    # see if computer can still recognise the speech
    recog = sr.Recognizer()  # create a reconiser
    input = sr.AudioFile("./filtered.wav")
    with input as source:
        audio = recog.record(source)  # pull in audio signal from file
    try:
        result = recog.recognize_sphinx(audio)
        print(result)  # use pocketsphinx to recognise the speech
    except:  # if it can't tell what it is it throws an exception, so catch it
        print("Can't recognise speech")
    return


def examine(): #function for examining the responses of yes/no to try and make a template for the matched filter
    directory_in_str = "./Dataset/yes_women/"  # define directory of files to recognise
    directory = os.fsencode(directory_in_str)
    average = AudioSegment.silent(duration=1000) #silence for 1s as starting point to add other stuff onto
    count =0
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".wav"):
            audio = AudioSegment.from_file(directory_in_str+filename)
            average = average.overlay(audio)
            count=count+1
    play(average)
    avg_samples = average.get_array_of_samples()
    avg_samples = np.divide(avg_samples,count)
    plt.plot(avg_samples)
    plt.show()

    avg_sound = average._spawn(avg_samples)
    play(avg_sound)
    return

def matchedFilterTest():
    # Load signals
    template1 = AudioSegment.from_file("./Dataset/yes/0a7c2a8d_nohash_0.wav") # a random woman saying yes
    template2 = AudioSegment.from_file("./Dataset/no/0b40aa8e_nohash_0.wav") #female no
    template3 = AudioSegment.from_file("./Dataset/yes/0135f3f2_nohash_0.wav") # male yes
    template4 = AudioSegment.from_file("./Dataset/no/0b56bcfe_nohash_0.wav") #male no

    input = AudioSegment.from_file("./Dataset/yes/00f0204f_nohash_0.wav") #input signal
    noise = AudioSegment.from_file("./Household Noise/cat.wav") #cat noise
    noisy_input =noise.overlay(input) #create a noisy signal

    #convert from audiosegment to samples
    template_samples1 = template1.get_array_of_samples() #get np array of samples so they can be filtered
    template_samples2 = template2.get_array_of_samples()
    template_samples3 = template3.get_array_of_samples()
    template_samples4 = template4.get_array_of_samples()

    noisy_input_samples = noisy_input.get_array_of_samples()

    #MSE compared to templates
    mse = mean_squared_error(noisy_input_samples,template_samples1) #yes template
    mse2 = mean_squared_error(noisy_input_samples, template_samples2) #no template
    mse3 = mean_squared_error(noisy_input_samples, template_samples3) # male yes
    mse4 = mean_squared_error(noisy_input_samples,template_samples4) #male no

    #display results
    print("MSE WOMEN YES =", mse)
    print("MSE WOMEN NO =", mse2)
    print("MSE MEN YES =", mse3)
    print("MSE MEN NO =", mse4)

    plt.subplot(121)
    plt.plot(template_samples1)
    plt.title('Ideal signal')
    plt.subplot(122)
    plt.plot(noisy_input_samples)
    plt.title('Noisy signal')

    return

def MSEtestWithAllFiles():
    noise = AudioSegment.from_file("./Household Noise/music.wav")  # cat noise
    directory_in_str = "./Dataset/no/"  # define the directory of files to recognise
    directory = os.fsencode(directory_in_str)
    count = 0
    avg1 = 0
    avg2 = 0
    avg3 = 0
    avg4 = 0
    correct = 0  # right word, right gender
    partially_correct = 0  # right word, wrong gender
    incorrect = 0  # wrong word, wrong gender
    partially_incorrect = 0  # right gender, wrong word
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".wav"):
            input = AudioSegment.from_file(directory_in_str + filename)
            noisy_input = input.overlay(noise)  # create a noisy signal
            # noisy_input_samples = input.get_array_of_samples() #get array of samples
            wy, wn, my, mn, filtered_file = checkMSE(noisy_input)
            avg1 = avg1 + wy
            avg2 = avg2 + wn
            avg3 = avg3 + my
            avg4 = avg4 + mn
            if wy < wn and wy < my and wy < mn:  # if women yes is lowest
                correct = correct + 1
            elif my < wy and my < wn and my < mn:  # if man yes is lowest
                correct = correct + 1
            elif wn < wy and wn < my and wn < mn:  # if woman no is lowest
                incorrect = incorrect + 1
            elif mn < wy and mn < wn and mn < my:  # if man no is lowest
                incorrect = incorrect + 1
            print(count)
            count = count + 1

    # display results
    print("NO FILES =", count)
    print("MSE WOMEN YES =", avg1 / count)
    print("MSE WOMEN NO =", avg2 / count)
    print("MSE MEN YES =", avg3 / count)
    print("MSE MEN NO =", avg4 / count)
    print("RIGHT WORD, RIGHT GENDER = ", correct)
    print("RIGHT WORD, WRONG GENDER =", partially_correct)
    print("WRONG WORD, RIGHT GENDER =", partially_incorrect)
    print("WRONG WORD, WRONG GENDER =", incorrect)
    return