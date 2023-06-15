#python text convert into  voice

import gtts
import playsound

text=input("Enter Something here : ")

sound = gtts.gTTS(text, lang="gu")

sound.save("welcome.mp3")
playsound.playsound("welcome.mp3")