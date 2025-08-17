import time
from plyer import notification
def send_notification(title,message):
    notification.notify(
        title=title,
        message=message,
        timeout=10
        )
        
def study_remainder():
    print("Welcome to study remainder Bot!")
    study_minutes=int(input("enter study duration:"))
    break_minutes=int(input("Enetr break duration:"))
    cycles=int(input("Enetr number of study-break cycles:"))
    study_seconds=study_minutes*60
    break_seconds=break_minutes*60
    for cycle in range(1,cycles+1):
        print(f"\nCycle {cycle}/{cycles}: Time to STUDY!")
        send_notification("📚 Study Time!", f"Cycle {cycle}: Focus for {study_minutes} minutes.")
        time.sleep(study_seconds)
        print("Study session complete> Time For a break!")
        send_notification("Break Time!", f"Relax for {break_minutes} minutes.")
        time.sleep(break_seconds)
    print("\nAll study Cycles completed! Great Job!")
    send_notification("Done you have completed all study cycles")
study_remainder()
