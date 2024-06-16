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
    speak("Initializing......")
    while True:
        #Listerning for the wakeup
        r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e)) 
    