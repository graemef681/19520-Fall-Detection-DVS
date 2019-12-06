from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from pygame import mixer #easy way to play mp3

def createFiles():
    #Function to connect to gTTS and create tts files
    #not needed in day-to-day running, only needed once
    #since files won't change
    tts = gTTS(text='Do you need an ambulance?',lang='en',slow = False)
    tts.save("./q1.mp3")

    tts = gTTS(text ='Do you need your named contact?')
    tts.save("./q2.mp3")

    tts = gTTS(text ='Do you need help?',lang='en',slow = False)
    tts.save("./q3.mp3")

    tts = gTTS(text='Calling an ambulance', lang='en', slow=False)
    tts.save("./r1.mp3")

    tts = gTTS(text='Calling named contact', lang='en', slow=False)
    tts.save("./r2.mp3")

    tts = gTTS(text='Turning System Off', lang='en', slow=False)
    tts.save("./r3.mp3")

    return

def speak(type, number):
    responseType ="./"+ type + str(number) + ".wav"
    mixer.init()
    mixer.music.load('e:/LOCAL/Betrayer/Metalik Klinik1-Anak Sekolah.mp3')
    mixer.music.play()

    return