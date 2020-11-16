from tkinter import *
from random import choice

colors_list = ["red", "blue", "green", "yellow", "purple", "cyan"]
button_number = 0
total_colors = []
stored_colors = []
row = 0
column = 0
difficulty = 1

"Color_list is list of all possible unique colors."
"Button_number is the total blocks present on the game."
"Total_colors is all the colors of the game in the order of the button_number."
"Stored_colors stores the colors from the blocks which the user has picked."
"Difficulty controls the number of blocks the game creates."


class main_window:
    def __init__(self):
        self.root = Tk()
        self.root.title("Main Window")

    "The function below creates a button and then opens the canvas function when clicked."
    "Color for the button is the same as the color of the canvas."

    def button(self, column, row, button_number, color, stored):
        button = Button(text=("Button", button_number), bg="black",
                        width=20, height=10, command=lambda: [self.canvas(column, row, color, stored)
                                                              ], activebackground=color)
        button.grid(column=column, row=row)

    "The function below checks and replaces if any randomly picked color from the color_list is not the same."
    "The difficulty increases the number of same colors allowed."

    def no_more_than_two_colors(self, color):
        while total_colors.count(color) >= (2 * difficulty):
            color = choice(colors_list)
        return color

    "The function below places a canvas when the button is clicked."
    "The function below then stores the color of the canvas to the stored list."
    "We need to create a list of canvases the user opened to delete them when user picks wrong colors."
    "Then create the if statements to compare to zeroth color with first color in the stored (stored_colors)"
    "We will do this later."

    def canvas(self, column, row, color, stored):
        canvas = Canvas(self.root, bg=color, width=145, height=150)
        canvas.grid(column=column, row=row)
        stored += [color]
        print(stored)
        return stored


window = main_window()
"Creates a main window for the game"

"The for loop below creates buttons and canvas based the number of the unique colors multiplied by 2."
"This changes depending on the difficulty the user has picked."

for color in colors_list * 2 * difficulty:

    "Then the for loop randomly picks a color from the color_list."

    color = choice(colors_list)

    "Then the function no_more_than_two_colors is called to check and randomly replace the same color."

    color = window.no_more_than_two_colors(color)

    "The if statement is used to create widgets on the first three column (The button number can be used as well)."

    if column % 3 == 0:
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
