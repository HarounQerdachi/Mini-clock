import flet as ft
import time
import threading

def main(page: ft.Page):
    page.title = "Mini clock - by HarounQerdachi"
    page.window_width = 1000
    page.window_height = 550
    page.theme_mode = "dark"
    page.window_resizable = False

    page.fonts = {
        "Open Sans Regular": "fonts/OpenSans-Regular.ttf",
        "Open Sans Italic": "fonts/OpenSans-Italic.ttf",
        "Open Sans Light": "fonts/OpenSans-Light.ttf",
        "Open Sans SemiBold": "fonts/OpenSans-SemiBold.ttf",
        "Fanlste": "fonts/fanlste.otf",
    }

    def countdown_timer(minutes):
        total_seconds = minutes * 60
        for _ in range(total_seconds, -1, -1):
            if stop_countdown_flag.is_set():
                break  # Stop the countdown if the flag is set
            mins, secs = divmod(_, 60)
            counter.value = '{:02d}:{:02d}'.format(mins, secs)
            page.update()
            time.sleep(1)
        counter.value = 'Countdown Complete'
        page.update()

    def start_countdown(event):
        try:
            stop_countdown_flag.clear()  # Clear the flag before starting a new countdown
            threading.Thread(target=countdown_timer, args=(int(the_time.value),)).start()
            error_label.value = ''
        except ValueError:
            error_label.value = "Invalid value entered. Please enter a valid integer."

    def stop_countdown(event):
        stop_countdown_flag.set()  # Set the flag to stop the ongoing countdown

    the_time = ft.TextField(label="Insert time in minutes")
    counter = ft.Text(size=90, font_family='Open Sans Light')
    error_label = ft.Text(color='red', font_family='Open Sans Regular')
    stop_button = ft.ElevatedButton("Stop Countdown", on_click=stop_countdown)
    stop_countdown_flag = threading.Event()  # Event flag to signal when to stop the countdown

    bt = ft.ElevatedButton("Start Countdown", on_click=start_countdown)

    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Mini Clock", size=24, color="white", font_family='Fanlste'),
                    ft.Text("The pomodoro timer that empowers you to take control \nof your time and optimize your work sessions.",
                            size=14, color="white", font_family='Open Sans Italic', text_align='center'),
                    counter,
                    the_time,
                    bt,
                    stop_button,
                    error_label,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            margin=ft.margin.only(top=20),
            alignment=ft.alignment.center,
        ),
    )


ft.app(target=main, assets_dir="../assets")