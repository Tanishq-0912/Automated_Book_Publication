# Directory: voice/voice_interface.py
import pyttsx3

def read_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
