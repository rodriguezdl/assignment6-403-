#####################################################
# Daniel Rodriguez
# Assignment 6
# Due Thursday April 25, 2019
# ###################################################

#from rectpack import newPacker
from tkinter import *


#
#Inficates that tkinter can be imported whether the ber
# of python is 3 or below.
#try:
#    from Tkinter import *
#except ImportError:
#    from tkinter import *

# Constructor for canvas creation. Initialises height and width variables
# That are passed in via main and renders the rectangles using
# tkinter library/
# import tkinter as tk

class CustomCanvas:
    def __init__(self, height, width):  # canvas size
        self.height = height
        self.width = width

    def render_rectangles(self, rect_list):
        master = Tk()
        canvas = Canvas(master, height=self.height, width=self.width)
        canvas.pack()
        for rectangle in rect_list:
            canvas.create_rectangle(rectangle.x, rectangle.y, rectangle.x + rectangle.width, rectangle.y + rectangle.height)

# Constructors for the rectangle object. Sets values for
# different aspects points of the rectangle

class Rectangle:
    # initialise the variables for rectangle, with x and y initially 0 to start at top left most corner of canvas
    def __init__(self, height, width, x=0, y=0):
        self.height = height
        self.width = width
        self.x = x
        self.y = y


#Takes rpack function from rectangle-packer external library and paks the rectangles

def pack(allRect):
  CustomCanvas.width = allRect[0][0]
  CustomCanvas.height= allRect[0][1]
  dimension_values = allRect[1:]
  # print(dimension_values)
  # for i in allRect:
  #      for j in allRect:
  #         rect = Rectangle(allRect[i][j], allRect[i][j+1])
  CustomCanvas.render_rectangles(dimension_values)



# Main method: where system arguments are handles and values from text file are taken so that
# files can be rendered upon the canvas.

def main():
    i = 0
    path = sys.argv[1]  # allow for 2nd argument to be file path desired and opened
    path = open(path, 'r')
    dimension_values = []
    for line in path:  # iterate through the lines within the file
        line = line.strip().split(",")
        dimension_values.append(line)


    pack(dimension_values)


# call to main function
if __name__ == "__main__":
    main()
