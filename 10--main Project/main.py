import speech_recognition as sr
import webbrowser
import pyttsx3
import music
import time

# initialize
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    c = c.lower()

    if "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open facebook" in c:
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")

    elif "open linkedin" in c:
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")
        
    elif c.startswith("play"):
     song = c.replace("play", "").strip()
     speak(f"Playing {song} on YouTube")
     webbrowser.open(f"https://www.youtube.com/results?search_query={song}")

    # elif c.startswith("play"):
    #     song = c.replace("play", "").strip()
    #     if song in music.m:
    #         speak(f"Playing {song}")
    #         webbrowser.open(music.m[song])
    else:
            speak("Sorry, song not found")



if __name__ == "__main__":
    speak("Initializing Jarvis")
    time.sleep(1)

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source, phrase_time_limit=4)

            text = recognizer.recognize_google(audio, language="en-US")
            print("You said:", text)

            # ✅ WAKE WORD FIX
            if "jarvis" in text.lower():
                speak("Yes")

                with sr.Microphone() as source:
                    print("Jarvis active, listening for command...")
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio, language="en-US")
                print("Command:", command)
                processcommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError:
            print("Internet problem")
