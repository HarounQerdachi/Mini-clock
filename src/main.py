import time

session_length_minutes = int(input("Enter the length of each session in minutes: "))

for x in reversed(range(0, session_length_minutes * 60)):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    timer_display = f"{hours:02}:{minutes:02}:{seconds:02}"
    print(timer_display, end='\r')
    time.sleep(1)

print("\nSession complete!")
