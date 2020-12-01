from tkinter import *
from tkinter import messagebox
from random import choice

colors_list = ["red", "blue", "green", "cyan", "magenta", "purple", "orange", "yellow"]
button_number = 0
total_colors = []
stored_colors = []
row = 0
column = 0
canvas_list = []
succes_colors = []
difficulty = 1


"Color_list is list of all possible unique colors."
"Button_number is the total blocks present on the game."
"Total_colors is all the colors of the game in order of the button_number."
"Stored_colors stores the colors from the blocks which the user has picked."
"Difficulty controls the number of blocks the game creates."


class main_window:
    def __init__(self):
        self.root = Tk()
        self.root.title("Main Window")

    "The function below creates a button and then opens the canvas function when clicked."
    "Color for the button is the same as the color of the canvas."

    def button(self, column, row, button_number, color, store):

        button = Button(text=("Button", button_number), bg="black",
                        width=19, height=9,
                        command=lambda: [
                            self.canvas(column, row, color, canvas_list, store, succes_colors)
                                         ], activebackground=color)
        button.grid(column=column, row=row)

    "The function below checks and replaces if any randomly picked color from the color_list is not the same."

    def no_more_than_two_colors(self, color):
        while total_colors.count(color) > 1:
            color = choice(colors_list)
        return color

    "The function below places a canvas when the button is clicked."
    "The function below then stores the color of the canvas to the stored list."
    "We need to create a list of canvases the user opened to delete them when user picks the wrong colors."
    "Then create the if statements to compare to zeroth color with first color in the stored (stored_colors)"
    "We will do this later."

    def canvas(self, column, row, color, canvas_list, stored_colors, succes_colors):
        canvas = Canvas(self.root, bg=color, width=139, height=142)
        canvas.grid(column=column, row=row)
        canvas_list += [canvas]
        stored_colors.append(color)
        if len(stored_colors) == 2:
            if stored_colors[1] == stored_colors[0]:
                succes_colors += canvas_list
            else:
                for x in succes_colors:
                    if x in canvas_list:
                        canvas_list.remove(x)
                if len(canvas_list) == 2:
                    for c in canvas_list:
                        c.destroy()
                canvas_list.clear()
            stored_colors.clear()
        return canvas_list, succes_colors

window = main_window()
"Creates a main window for the game"

"The for loop below creates buttons and canvas based the number of the unique colors multiplied by 2."

for color in colors_list * 2:

    "Then the for loop randomly picks a color from the color_list."

    color = choice(colors_list)

    "Then the function no_more_than_two_colors is called to check and randomly replace same color."

    color = window.no_more_than_two_colors(color)

    "The if statement is used to create widgets on the first three column (The button number can be used as well)."

    if column % 4 == 0:
        "Then create widgets on the first three columns of the next row."

        row += 1
        column = 0

    "After the if statement, both the color, row number and the column number is sent to the button()."
    "The button() then places the button on the said column and row number."
    "Button() then calls the canvas() to be place in the same position."

    window.button(row, column, button_number, color, stored_colors)

    "Calculate the next column"

    column += 1

    "The total_colors stores the colors in the order of the button_numbers(total columns)"

    total_colors += [color]

    "Button_number is the total blocks present on the game."

    button_number += 1

print(total_colors)
window.root.mainloop()
