from typing import Dict, List

from canvas import Canvas
from shapes import Rectangle, Square

# Taking user's input to create the canvas
canvas_width=int(input("Please enter the canvas width: "))
canvas_height=int(input("Please enter the canvas height: "))

# Prompt for colour from user
color = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color=input("Please enter the canvas colour(white or black): ")

# Creating a canvas with user's input data
main_canvas= Canvas(canvas_width, canvas_height, color=color[canvas_color])


while True:
    shape_type=input("What would you like to paint? Enter quite to finish.")

    if shape_type.lower()=='rectangle':

        rectangle_x=int(input("Enter the x of the rectangle: "))
        rectangle_y=int(input("Enter the y of the rectangle: "))
        rectangle_width=int(input("Enter rectangle's width: "))
        rectangle_height=int(input("Enter rectangle's height: "))
        red=int(input("How much red should be added? Keep it between 0 to 255. "))
        green=int(input("How much green? Keep it between 0 to 255. "))
        blue=int(input("How much blue? Keep it between 0 to 255. "))

        rectangle=Rectangle(rectangle_x, rectangle_y,
                            rectangle_height, rectangle_width,
                            color=[red, green, blue])
        rectangle.draw(canvas=main_canvas)

    if shape_type.lower()=='square':
        sq_x=int(input("Enter the x of square: "))
        sq_y=int(input("Enter the y of square: "))
        sq_side=int(input("Enter the side of the square: "))
        red = int(input("How much red should be added? Keep it between 0 to 255. "))
        green = int(input("How much green? Keep it between 0 to 255. "))
        blue = int(input("How much blue? Keep it between 0 to 255. "))

        square=Square(sq_x,sq_y, sq_side, color=[red, green, blue])
        square.draw(canvas=main_canvas)



    if shape_type.lower()=='quit':
        break


main_canvas.make("canvas.png")









square= Square(10, 10, 30, [150, 250, 0])
square.draw(canvas=main_canvas)

rectangle= Rectangle(40, 40, 30, 20, [0, 0, 250])
rectangle.draw(canvas=main_canvas)

main_canvas.make("img1.png")