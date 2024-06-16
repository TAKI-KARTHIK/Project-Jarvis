import speech_recognition as sr
import webbrowser
import pyttsx3
import music_Library

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def process_Command(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1] 
        link = music_Library.music[song]
        webbrowser.open(link)

#what does song = c.lower().split(" ")[1] command do,
# if we say play cartoon, it just split these word into a list like ["play", "cartoon"] and it search for the index value 1
#that is cartoon (index value always starts with 0)

#Python's if __name__ == "__main__": construct enables a single Python file to not only support reusable code and functions, but also contain executable code that will not explicitly run when a module is imported.
if __name__ == "__main__":
    speak("Initializing......")
    while True:
        #Listerning for the wakeup word
        r = sr.Recognizer()
        print("Recognizing...")    
        try:
            with sr.Microphone() as source:
                print("Listerning..")
                audio = r.listen(source) #You can even add timeout and phrase_time_limit parameter
                word = r.recognize_google(audio)
                if(word.lower() == "jarvis"):
                   speak("Yes sir, How can i help you")
                   #listerning for the userinput
                   with sr.Microphone() as source:
                       print("Jarvis Active..")
                       audio = r.listen(source)
                       command = r.recognize_google(audio)

                       process_Command(command)


        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e)) 
    