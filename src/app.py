import flet as ft

def main(page: ft.Page):
    # Set a title and adding some color to the background
    page.title= "Mini clock"
    page.bgcolor= "#323232"

    # Set the width and the height of the app
    page.window_width= 1000
    page.window_height= 550
    # page.theme_mode= "dark"

    # Disable resizing the app
    page.window_resizable= False

    #Adding fonts
    page.fonts= {
            "Open Sans": "fonts/OpenSans-Regular.ttf",
            "Fanlste": "fonts/fanlste.otf",
        }

    title= ft.Text(value= "Mini Clock", size= 28, weight= "w700", color= "white", font_family= 'Open Sans', text_align="center")
    description= ft.Text(value= "The pomodoro timer that empowers you to take control of your time and optimize your work sessions.", size= 14, color= "white", font_family= 'Open Sans',)

    page.add(
        title, description
    )

    page.update()

ft.app(target=main, assets_dir="../assets")