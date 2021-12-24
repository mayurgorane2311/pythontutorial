## Healthey programmer___________________________!
from time import time
from datetime import datetime
from pygame import mixer

# # Starting the mixer
# mixer.init()
# # Loading the song
# mixer.music.load("exe.mp3")
#
# # Setting the volume
# mixer.music.set_volume(1)
#
# # Start playing the song
# mixer.music.play()
#
# # infinite loop
# while True:
#
#     print("Press 'p' to pause, 'r' to resume")
#     print("Press 'e' to exit the program")
#     query = input("  ")
#
#     if query == 'p':
#
#         # Pausing the music
#         mixer.music.pause()
#     elif query == 'r':
#
#         # Resuming the music
#         mixer.music.unpause()
#     elif query == 'e':
#
#         # Stop the mixer
#         mixer.music.stop()
#         break

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    f = open("summery.txt","a")
    f.write(f"{msg} {datetime.now()}\n")

inti_water = time()
inti_eye = time()
inti_exercise = time()
watertime = 60
eyetime =   160
exetime =   250

while True:
    if time()-inti_water >watertime:
        print("your water drank time.Enter 'drank' to stop alarm  ")
        musiconloop("Water.mp3","d")
        inti_water
        log_now("drank water at")

    if time()-inti_eye > eyetime:
        print("your eye Exercise time.Enter 'done' to stop alarm  ")
        musiconloop("eye.mp3","d")
        inti_eye
        log_now("Eye exercise at")

    if time()-inti_exercise > exetime:
        print("your Worm up time.Enter 'ok' to stop alarm  ")
        musiconloop("exe.mp3","d")
        inti_exercise
        log_now("worm  up activity exercise at")





