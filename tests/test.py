# for the margin, place your text column into a container, and set the container's margin to x from the top (eg: flet.margin.only(top = 20))
# for the center alignment, set the column's horizontal_alignment to flet.CrossAxisAlignment.CENTER

# i recommend you use flet's enums instead of typing out "center" in a string

# example:
# flet.Container(
#     content = flet.Column(
#         controls = [
#             flet.Text("gggg"),
#             flet.Text("hhhhh")
#         ],

#         alignment = flet.MainAxisAlignment.CENTER
#     ),
    
#     margin = flet.margin.only(top = 20), # add some space between the top of the container and the page
#     alignment = flet.alignment.center, # horizontally align the column (and its controls) to the center
#     expand = True
# )

import asyncio
import flet as ft

class Countdown(ft.UserControl):
    def __init__(self, seconds):
        super().__init__()
        self.seconds = seconds

    async def did_mount_async(self):
        self.running = True
        asyncio.create_task(self.update_timer())

    async def will_unmount_async(self):
        self.running = False

    async def update_timer(self):
        while self.seconds and self.running:
            mins, secs = divmod(self.seconds, 60)
            self.countdown.value = "{:02d}:{:02d}".format(mins, secs)
            await self.update_async()
            await asyncio.sleep(1)
            self.seconds -= 1

    def build(self):
        self.countdown = ft.Text()
        return self.countdown

async def main(page: ft.Page):
    await page.add_async(Countdown(120), Countdown(60))

ft.app(target=main)