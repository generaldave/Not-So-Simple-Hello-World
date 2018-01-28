'''
David Fuller

Pixelizer class: Class to handle creating and displaying pixels based on
a given text input.

1-28-2018
'''

from PIL import Image, ImageFont, ImageDraw
import random

from .Constants import *

class Pixelizer(object):
    '''
    Sets up a Pixelizer object.
    '''
    
    def __init__(self, message, surface_resolution):
        '''
        App's init method.

        Stores pixelizer attributes.

        Args:
            message (str): Message to pixelize.
            surface_resolution (resulotion): Width and height of surface.
        '''
        
        self.size = resolution(width = 1, height = 1)

        self.pixels = []

        self.pixelize_message(message, surface_resolution)

    def pixelize_message(self, message, surface_resolution):
        '''
        Pixelizes a given message.

        Args:
            message (str): Message to pixelize.
            surface_resolution (resulotion): Width and height of surface.
        '''
        
        font = ImageFont.truetype(arial_bold, font_size)
        
        text_width, text_height = font.getsize(message)

        text_x = int(surface_resolution.width / 2 - text_width / 2)
        text_y = int(surface_resolution.height / 2 - text_height / 2) - 14

        position = point(x = text_x, y = text_y)
        size = resolution(width = text_width + text_x,
                          height = text_height + text_y)

        image = Image.new(black_and_white, size, black)
        draw = ImageDraw.Draw(image)

        draw.text(position, message, font = font)

        for i in range(size.height):
            for j in range(size.width):
                position = point(x = j, y = i)
                if not image.getpixel(position):
                    self.pixels.append(position)

    def show_one(self, surface, surface_resolution):
        '''
        Shows one pixel in a random location.

        Args:
            surface (pygame.surface): Surface to show pixel on.
            surface_resolution (resulotion): Width and height of surface.
        '''
        
        position = point(x = random.randint(0, surface_resolution.width),
                         y = random.randint(0, surface_resolution.height))

        if position in self.pixels:
            pixel_color = color(r = 0, g = 0, b = 255)
        else:
            pixel_color = color(r = random.randint(0, 255),
                                g = random.randint(0, 255),
                                b = random.randint(0, 255))

        surface.fill(pixel_color, (position, self.size))
            

    def show_text_image(self):
        '''
        Shows the message as an image.
        '''
        
        self.image.show()
        
        
