import pydub
from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt
from operator import sub
#Pydub has functions for high pass and low pass filters we can use to bandpass

def bandpassSignal(filename):
    signal = AudioSegment.from_file(filename)
    lpSignal = signal.low_pass_filter(300)
    bpSignal = lpSignal.high_pass_filter(34000)
    return bpSignal

def removeNoise(signal_AS, template_AS):
    signal = signal_AS.get_array_of_samples()
    template = template_AS.get_array_of_samples()
    signal_fft = np.fft.fft(signal[0:16000])
    template_fft = np.fft.fft(template)
    noise_fft = signal_fft-template_fft
    clean_fft = signal_fft-(noise_fft/2)
    result = np.fft.ifft(clean_fft)

    '''
    plt.subplot(141)
    plt.plot(template)
    plt.title("Template")
    plt.subplot(142)
    plt.plot(signal)
    plt.title('Noisy Signal')
    plt.subplot(143)
    plt.plot(result)
    plt.title('Clean signal')
    plt.show()
    '''

    return result