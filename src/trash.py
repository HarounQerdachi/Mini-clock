import time

session_length_minutes = int(input("Enter the length of each session in minutes: "))
number_of_sessions = int(input("Enter the number of sessions that you want to do: "))
break_length_minutes = int(input("Enter the length of each break in minutes: "))

def session():   
    for x in reversed(range(0, session_length_minutes * 60)):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600)
        timer_display = f"{hours:02}:{minutes:02}:{seconds:02}"
        print(timer_display, end='\r')
        time.sleep(1)

def resting():
    for x in reversed(range(0, break_length_minutes * 60)):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600)
        timer_display = f"{hours:02}:{minutes:02}:{seconds:02}"
        print(timer_display, end='\r')
        time.sleep(1)

def main():
    for i in range(1 , number_of_sessions):
        session()
        resting()