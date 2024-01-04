import time

def countdown(minutes):
    for x in reversed(range(0, minutes * 60)):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600)
        timer_display = f"{hours:02}:{minutes:02}:{seconds:02}"
        print(timer_display, end='\r')
        time.sleep(1)

def perform_pomodoro(session_length, break_length, num_sessions):
    for i in range(num_sessions):
        print(f"\nSession {i + 1}/{num_sessions}")
        countdown(session_length)
        
        if i < num_sessions - 1:  # No break after the last session
            print("\nTake a break!")
            countdown(break_length)

def main():
    session_length_minutes = int(input("Enter the length of each session in minutes: "))
    number_of_sessions = int(input("Enter the number of sessions that you want to do: "))
    break_length_minutes = int(input("Enter the length of each break in minutes: "))

    perform_pomodoro(session_length_minutes, break_length_minutes, number_of_sessions)

if __name__ == "__main__":
    main()
