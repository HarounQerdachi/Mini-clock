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