import pyttsx3 as tts

def speak():
    engine = tts.init()
    voices = engine.getProperty('voices')  # getting details of current voice
    engine.setProperty('voice', voices[1].id)
    engine.say("Hello World!")
    engine.runAndWait()
    engine.stop()
    return
