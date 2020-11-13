from tkinter import * # for GUI
import random # randomly pick color


colors = ["red", "blue", "green", "yellow", "purple", "cyan"] # list of colors
red_numb = 0
blue_numb = 0
green_num = 0
yellow_numb = 0
purple_numb = 0
cyan_numb = 0
root = Tk() # main window
root.geometry("600x480") # resolution of the program when its starts
root.title("Main window") # title of the program
row = 0
column = 0
i = 0

def button(row, column, buttonnumb, color): # function to place buttons
    button = Button(root, text=("Button",buttonnumb), command= lambda : colored_blocked(row, column, buttonnumb, color),
                    height=10, width=20, bg="black") # place the buttons and show the colored blocks when clicked
    button.grid(column=row, row=column) # display the buttons

def colored_blocked(row, column, buttonnumb, color): # funtion for showing the coloreed blocks when button is clicked
    print(row, column, buttonnumb, color) # which row and column is the block and which button number and color
    canvas = Canvas(root, bg=color, height=100, width=100) # place the colored blocks
    canvas.grid(column=row, row=column) # show the colored block
def check_color(color1, color2): # Incomplete
    if color1 == color2:
        print("same color")
def same_color(totalcolor, color): # check if colors are repeated
    print(totalcolor, color)
    while totalcolor >= 4:
        print(colors)
        d = random.choice(colors) # randomly pick another color
        return d
    else:
        return color

for c in colors*2: # loop to create 12 buttons and colored blocks
    c = random.choice(colors) # randomly select colored blocks, c is the color
    if c == 'red': # check if there are more than 2 red blocks
        red_numb += 1
        if red_numb > 1:
            colors.remove(c)
            c = same_color(red_numb, c)
    elif c == "blue": # check if there are more than 2 blue blocks
        blue_numb += 1
        if blue_numb > 1:
            colors.remove(c)
            c = same_color(blue_numb, c)
    elif c == "green": # check if there are more than 2 green blocks
        green_num += 1
        if green_num > 1:
            colors.remove(c)
            c = same_color(green_num, c)
    elif c == "yellow": # check if there are more than 2 yellow blocks
        yellow_numb += 1
        if yellow_numb > 1:
            colors.remove(c)
            c = same_color(yellow_numb, c)
    elif c == "purple": # check if there are more than 2 purple blocks
        purple_numb += 1
        if purple_numb > 1:
            colors.remove(c)
            c = same_color(purple_numb, c)
    elif c == "cyan": # check if there are more than 2 cyan blocks
        cyan_numb += 1
        if cyan_numb > 1:
            colors.remove(c)
            c = same_color(cyan_numb, c)
    if i <= 2: # place 3 buttons and colored blocks in first row
        button(row, column,i,c)
        column += 1
    elif  3 <= i <= 5: # place 3 buttons and colored blocks in second row
        if i == 3:
            column = 0
        row = 1
        button(row, column,i,c)
        column += 1
    elif 6 <= i <= 8: # place 3 buttons and colored blocks in third row
        if i == 6:
            column = 0
        row = 2
        button(row, column,i,c)
        column += 1
    elif 9 <= i <= 11: # place 3 buttons and colored blocks in fourth row
        if i == 9:
            column = 0
        row = 3
        button(row, column,i,c)
        column += 1
    i += 1 # this the button number
root.mainloop() # display the GUI