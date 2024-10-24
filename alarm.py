from datetime import datetime, timedelta
from playsound import playsound
import time

def set_alarm(alarm_time):
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("Alarm ringing!")
            playsound('alarm-sound.mp3')  # Replace with your sound file path
            return  # Exit the function after ringing the alarm
        time.sleep(60)  # Check every minute

def snooze_alarm(snooze_duration):
    print(f"Snoozing for {snooze_duration} minutes...")
    time.sleep(snooze_duration * 60)  # Convert minutes to seconds

if __name__ == "__main__":
    alarm_time = input("Enter alarm time (HH:MM format): ")
    snooze_duration = int(input("Enter snooze duration in minutes: "))

    while True:
        set_alarm(alarm_time)
        snooze = input("Do you want to snooze? (yes/no): ").strip().lower()
        if snooze == 'yes':
            snooze_alarm(snooze_duration)
            # Update the alarm time to the new snooze time
            alarm_time = (datetime.now() + timedelta(minutes=snooze_duration)).strftime("%H:%M")
        else:
            print("Alarm stopped.")
            break