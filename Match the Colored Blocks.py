from tkinter import *
from tkinter import messagebox
from random import choice

colors_list = ["red", "blue", "green", "cyan", "magenta", "pink", "orange", "yellow"]
button_number = 0
total_colors = []
stored_colors = []
row = 0
column = 0
canvas_list = []
matched_canvas = []

'''
Color_list is list of all possible unique colors.
Button_number is the total blocks present on the game.
Total_colors is all the colors of the game in order of the button_number.
Stored_colors stores the colors from the blocks which the user has picked.
'''


class main_window:
    def __init__(self):
        self.root = Tk()
        self.root.title("Main Window")

    '''
    The function below creates a button and then opens the canvas function when clicked.
    Color for the button is the same as the color of the canvas.
    '''

    def button(self, column, row, button_number, color, store):

        button = Button(text=("Button", button_number), bg="black",
                        width=19, height=9,
                        command=lambda: [
                            self.canvas(column, row, color, canvas_list, store, matched_canvas)
                        ], activebackground=color)
        button.grid(column=column, row=row)

    # The function below checks and replaces if any randomly picked color from the color_list is not same.

    def no_more_than_two_colors(self, color):
        while total_colors.count(color) > 1:
            color = choice(colors_list)
        return color

    '''
    The function below places a canvas when the button is clicked.
    The function below then stores the color of the canvas to the stored list.
    Then create a list of canvases the user opened to delete them when user picks the wrong colors.
    Then create the if statements to compare to first color with the second color in the stored_colors.
    '''

    def canvas(self, column, row, color, canvas_list, stored_colors, matched_canvas):
        canvas = Canvas(self.root, bg=color, width=139, height=142)
        canvas.grid(column=column, row=row)

        # The code below recognizes the matched colors and deletes the first two canvases with different colors.

        canvas_list.append(canvas)
        stored_colors.append(color)

        '''
        The two lists above stores the color and canvases.
        The if statement checks if there are two canvases in the list.
        '''

        if len(canvas_list) == 2:

            # There is another if statement to check if the color of the second canvas is same as the first canvas.

            if stored_colors[1] == stored_colors[0]:

                # If true then create a windows which tells the user that the colors match.

                messagebox.showinfo("Colors Match", "Colors Matched Successfully")

                # Then store the canvases that were matched to the matched_canvas.'

                matched_canvas += canvas_list
            else:
                '''
                If false then create a window which tells the user that the colors do not match
                Then create a for loop which takes one canvas(x) from the matched_canvas.
                '''

                messagebox.showinfo("Color Match", "Colors do not match")

                for one__canvas in matched_canvas:

                    '''
                    Then create a if statement that checks if the canvas(one__canvas) from the matched_canvas is in the
                    canvas_list 
                    '''

                    if one__canvas in canvas_list:
                        # If true then remove the canvas(one__canvas) from the canvas_list.

                        canvas_list.remove(one__canvas)

                # Then create a for loop which removes each canvas from the canvas_list

                for each_canvas in canvas_list:
                    each_canvas.destroy()

            # Then delete a the items from the list: canvas_list and stored_colors.

            canvas_list.clear()
            stored_colors.clear()
        return canvas_list, matched_canvas


window = main_window()

'''
Creates a main window for the game

The for loop below creates buttons and canvas based the number of the unique colors multiplied by 2.
'''

for color in colors_list * 2:

    # Then the for loop randomly picks a color from the color_list.

    color = choice(colors_list)

    # Then the function no_more_than_two_colors is called to check and randomly replace the same color.

    color = window.no_more_than_two_colors(color)

    # The if statement is used to create widgets on the first three column (The button number can be used as well).

    if column % 4 == 0:
        # Then create widgets on the first three columns of the next row.

        row += 1
        column = 0
    '''
    After the if statement, both the color, row number and the column number is sent to the button().
    The button() then places the button on the said column and row number.
    Button() then calls the canvas() to be place in the same position.
    '''

    window.button(row, column, button_number, color, stored_colors)

    # Calculate the next column

    column += 1

    # The total_colors stores the colors in the order of the button_numbers(total columns)

    total_colors += [color]

    # Button_number is the total blocks present on the game.

    button_number += 1

print(total_colors)
window.root.mainloop()
