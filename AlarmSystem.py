#from gtts import gTTS
#import os

#def trigger_alarm(volume=50):
    #alarm_message = "Warning! Smoke is detected. Please evacuate immediately"
    #tts = gTTS(text=alarm_message, lang='en')
    #tts.save("alarm.mp3")
    #os.system(f"start /MIN wmplayer /play /close {os.path.abspath('alarm.mp3')} /Volume {volume}")

#trigger_alarm(volume=35)



import pyttsx3
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    
    engine.runAndWait()


#def trigger_alarm(volume=50):
    #alarm_message = "Warning! Smoke is detected. Please evacuate immediately"
    #message = speak(alarm_message)
    #message.save("alarm.mp3")
    #os.system(f"start /MIN wmplayer /play /close {os.path.abspath(r"C:\Users\DEV ZION\Music\Tom_Odell_-_Another_Love_.mp3")} /Volume {volume}")

#trigger_alarm(volume = 35)   