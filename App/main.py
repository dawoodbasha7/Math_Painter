from PIL import Image
import numpy as np
import turtle

class Canvas:
    """Object where all shapes will be drawn on"""

    def __init__(self, canvas_width, canvas_height, color):
        self.canvas_width=canvas_width
        self.canvas_height=canvas_height
        self.color=color

        # create a 3D numpy array of zeros
        self.data=np.zeros((self.canvas_height, self.canvas_width, 3),
                           dtype=np.uint8)
        self.data[:]=self.color

    def make(self, imagepath):
        """ Convert the current array into an image file """
        img=Image.fromarray(self.data, 'RGB')
        img.save(imagepath)

class Rectangle:

    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width=width
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x: self.x+ self.height, self.y: self.y+self.width]=self.color

class Square:

    def __init__(self, x, y, side, color):
        self.x=x
        self.y=y
        self.side=side
        self.color=color


    def draw(self, canvas):
        canvas.data[self.x:self.x+self.side, self.y: self.y+self.side]= self.color




main_canvas=Canvas(100, 100, [250, 250, 250])

square=Square(10,10, 30, [0,250,0])
square.draw(canvas=main_canvas)

rectangle=Rectangle(40, 40, 30, 20, [0,0, 250])
rectangle.draw(canvas=main_canvas)

main_canvas.make("img1.png")