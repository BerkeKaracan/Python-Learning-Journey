import time
import os
import random
import pygame
from gtts import gTTS
pygame.mixer.init()
print("--- ROBO SPEAKER ---")
choice = ""
while True:
    choice = input('''
    1 - Transform
    For Exit : Q
    What would you like to do? : 
    ''').upper()
    if choice == "Q" :
        print("Bye")
        break
    elif choice == "1" :
        text = input("What is your paragraph :  ")
        print("Saved...")
        try:
            converter = gTTS(text = text, lang = "en", slow = False)
            print("Transforming ....")
            time.sleep(1)
            random_no = random.randint(1, 1000)
            file_name = f"Speaking_{random_no}.mp3"
            converter.save(file_name)
            pygame.mixer.music.load(file_name)
            print("Playing ....")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            pygame.mixer.music.unload()
            os.remove(file_name)
        except Exception as e:
            print(f"Somethings went wrong(Check your internet connection): {e}")
    else:
        print("Please enter a valid choice")
