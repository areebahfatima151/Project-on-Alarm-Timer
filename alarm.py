import winsound
import time

def alarm(seconds):
    time_elapsed = 0

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        time_left = seconds - time_elapsed

        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"\rTime Left: {minutes_left:02d}:{seconds_left:02d}", end="")

    print("\nTime's up!")
    winsound.PlaySound("alarmm.mp3", winsound.SND_FILENAME)

# Get input from user
minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds

alarm(total_seconds)