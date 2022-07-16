''' this is 
my first python code'''
import os  #importing the OS Module

from playsound import playsound
playsound('C:\Users\hm746\Downloads\Music\Full+Song+Tujhe+Kitna+Chahein+Aur+Film+Version+Kabir+Singh+Shahid+K+Kiara+A+Mithoon+Jubin.mp3')
import pyttsx3
engine = pyttsx3.init()
engine.say('''Twinkle twinkle Little Star 
How I wonder what you are 
Up above the world so high 
like a diamond in the sky.''')
engine.runAndWait()
print('''Twinkle twinkle Little Star 
How I wonder what you are 
Up above the world so high 
like a diamond in the sky.''')