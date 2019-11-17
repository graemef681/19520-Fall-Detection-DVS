import speech_recognition as sr
from pydub import AudioSegment
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from scipy.io.wavfile import write
from Filtering import *
from pydub.playback import play

def basic(filename): #basic speech recognition
    recog = sr.Recognizer()  # create a reconiser
    input = sr.AudioFile(filename)
    with input as source:
        audio = recog.record(source)  # pull in audio signal from file
    try:
        result = recog.recognize_sphinx(audio)  # use pocketsphinx to recognise the speech
    except:  # if it can't tell what it is it throws an exception, so catch it
        print("Can't recognise speech")
        result="Can't recognise speech"
    return result

def checkSimilarity(signal, template):
    signal_fft = np.fft.fft(signal[0:16000])
    template_fft = np.fft.fft(template)
    autocorr = np.fft.irfft(signal_fft * np.conj(template_fft))

    plt.plot(autocorr)
    plt.title("Autocorr")
    return max(autocorr)


def checkMSE(filtered):
    # Load templates
    template1 = AudioSegment.from_file("./Dataset/Template/0a7c2a8d_nohash_0.wav")  # a random woman saying yes
    template2 = AudioSegment.from_file("./Dataset/Template/0b40aa8e_nohash_0.wav")  # female no
    template3 = AudioSegment.from_file("./Dataset/Template/0135f3f2_nohash_0.wav")  # male yes
    template4 = AudioSegment.from_file("./Dataset/Template/0b56bcfe_nohash_0.wav")  # male no

    # convert from audiosegment to samples
    template_samples1 = template1.get_array_of_samples()  # get np array of samples so they can be filtered
    template_samples2 = template2.get_array_of_samples()
    template_samples3 = template3.get_array_of_samples()
    template_samples4 = template4.get_array_of_samples()

#    filtered_samples = filtered.get_array_of_samples()
    filtered_samples = filtered[0:16000]#truncate any of the signal that's longer than the template (because it's just noise)

    #Spectral filtering
   # filtered_samples = removeNoise(noisy_input_samples, template_to_check_samples)
    #filename = 'msetest.wav'
    #write(filename, 16000, np.int16(np.real(filtered_samples))) #output the file

    # MSE compared to templates
    mse1 = mean_squared_error(np.real(filtered_samples), template_samples1)  # yes template
    mse2 = mean_squared_error(np.real(filtered_samples), template_samples2)  # no template
    mse3 = mean_squared_error(np.real(filtered_samples), template_samples3)  # male yes
    mse4 = mean_squared_error(np.real(filtered_samples), template_samples4)  # male no

    return mse1,mse2,mse3,mse4

def fromMSEGuessWord(filtered):
    mse1, mse2, mse3, mse4 = checkMSE(filtered)

    test = min(mse1, mse2, mse3, mse4)
    if test == mse1 or test == mse3:
        # if yes is the lowest mse
        guess = "yes"
    else:
        # if no is the lowest mse
        guess = "no"

    return guess
