from gtts import gTTS
from playsound import playsound

# The text to convert to audio
text = "first time i'm using a package in next.py course"

# Create a gTTS object with the text and desired language
tts = gTTS(text=text, lang='en')

# Save the audio to a file
tts.save("exam.mp3")

# Play the audio file
playsound("exam.mp3")
