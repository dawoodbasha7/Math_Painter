import numpy as np
from PIL import Image


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