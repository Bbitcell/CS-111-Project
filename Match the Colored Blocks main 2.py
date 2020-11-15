from tkinter import *
from random import choice

colors_list = ["red", "blue", "green", "yellow", "purple", "cyan"]  # List of unique colors
button_number = 0
total_colors = []  # List of all colors in the game
stored_colors = []  # List of all colors the user picked
row = 0  # row number for placing buttons and canvas
column = 0  # column number for placing buttons and canvas
difficulty = 1  # Difficulty for the game, higher the difficulty more blocks are in the game


class main_window:
    def __init__(self):  # For creating a window
        self.root = Tk()
        self.root.title("Main Window")

    def button(self, column, row, button_number, color, stored):  # For placing multiple buttons on the game
        button = Button(text=("Button", button_number), bg="black",
                        width=20, height=10, command=lambda: [self.canvas(column, row, color, stored)
                                                              ], activebackground=color)
        "^ Main properties of the button, when button is clicked open the canvas function and transfer the properties to the canvas."
        button.grid(column=column, row=row)  # placing the buttons according to the row and column

    '''The function below makes sure that there are only a pair of colors (the pair of colors is then multiplied by difficulty)'''
    def no_more_than_two_colors(self, color):  # This function makes sure that there are only a pair of colors (the pair of colors is multiplied by difficulty)

        while total_colors.count(color) >= (2 * difficulty):  # How many same colors are allowed
            color = choice(colors_list)  # If the number of same color is more than 2 * difficulty then randomly pick a new color from the list
        return color

    def canvas(self, column, row, color, stored):  # For placing multiple canvases and record the colors the user picked
        canvas = Canvas(self.root, bg=color, width=145, height=150)  # main properties of the canvas
        canvas.grid(column=column, row=row)  # for placing the canvas according the row and column
        """Create a list of user picked colors"""
        stored += [color]  # store the color in this list
        print(stored)  # to see what colors the user has picked
        return stored  # This make sures that more than one color is stored in the list


window = main_window()  # create a main window for the game

'''This for loop is for placing more than one button and canvases'''

for color in colors_list * 2 * difficulty:  # there are 6 uniques colors, so we need another same set of colors to match. this is then multiplieed by difficulty
    color = choice(colors_list)  # randomly pick one of the unique colors
    color = window.no_more_than_two_colors(
        color)  # check if there are no more than two of the same colors (With difficulty this changes)
    if button_number % 3 == 0:  # if there are more than three buttons and canvases in the same row
        row += 1  # then place the button and canvas in the next row
        column = 0  # then place the button and canvas from the zeroth column
    window.button(row, column, button_number, color, stored_colors)  # place the buttons with written properties

    column += 1  # then place the buttons and canvas in the next column
    total_colors += [color]  # add the color to list which contains all the colors.
    button_number += 1  # what number of the button and canvas is, so that we easily identify know which color belongs the button and canvas, if not sure change the bg color of button to "white".

print(total_colors)  # show all the possible colors based on their button number
window.root.mainloop()  # display the game