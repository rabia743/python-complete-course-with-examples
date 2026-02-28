
# import pyttsx3

# # Engine start karo
# engine = pyttsx3.init()

# # Jo text bolna hai
# engine.say("Hello! How are you? I am beginner python developer .")

# # Speech run karo
# engine.runAndWait()
from gtts import gTTS
import os

text = "Hello, I am speaking using Google Text to Speech"
tts = gTTS(text=text, lang='en')
tts.save("voice.mp3")
os.system("start voice.mp3")  # Windows me play karne ke liye


