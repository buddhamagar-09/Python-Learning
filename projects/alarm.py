import pygame
import time as t
from pathlib import Path

pygame.mixer.init()

sound_path = Path(__file__).resolve().parent / "fire_alarm.mp3"

def alarm(seconds):
    time_elapsed = 0
    while time_elapsed < seconds :
        t.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"\rAlarm will sound in: {minutes_left:02d}:{seconds_left:02d}", end="", flush=True)
    print()


def main():
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

if __name__ == '__main__':
    main()