import speech_recognition as sr

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
