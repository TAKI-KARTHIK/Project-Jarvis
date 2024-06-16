import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()


#Python's if __name__ == "__main__": construct enables a single Python file to not only support reusable code and functions, but also contain executable code that will not explicitly run when a module is imported.
if __name__ == "__main__":
    speak("Listerning......")
    #