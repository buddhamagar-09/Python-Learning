"""
Alarm application that waits for a specified duration and then plays a sound alert.
This module uses pygame to play an MP3 sound file after a user-defined delay.
It displays a countdown timer in the format MM:SS showing the remaining time
until the alarm sounds.
Functions:
    alarm(seconds): Waits for the specified number of seconds and displays
                     a countdown timer. Note: Function name has a typo
                     (should be 'alarm').
Usage:
    1. User inputs the number of minutes to wait
    2. User inputs the number of seconds to wait
    3. Countdown timer is displayed
    4. After countdown completes, an MP3 sound file (fire_alarm.mp3)
       is played from the project directory
    5. Program waits until the sound finishes playing
Requirements:
    - pygame library for audio playback
    - fire_alarm.mp3 file in the same directory as this script
Note:
    - Sound file path is relative to the script's location
"""
import pygame
import time as t
from pathlib import Path

pygame.mixer.init()

sound_path = Path(__file__).resolve().parent / "fire_alarm.mp3"

def alarm(seconds):
    time_elapsed = 0
    print("Alarm will sound in: ", end="", flush=True)
    while time_elapsed < seconds :
        t.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"\rAlarm will sound in: {minutes_left:02d}:{seconds_left:02d}", end="", flush=True)
    print()

minutes = int(input("How many Minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes*60 + seconds

alarm(total_seconds)

if not sound_path.exists():
    print(f"Sound file not found: {sound_path}")
else:
    pygame.mixer.music.load(str(sound_path))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        t.sleep(0.1)