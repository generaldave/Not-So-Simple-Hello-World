########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Pixel Array Class: An array of pixels                                #
#                                                                      #
# Created on 2016-12-30                                                #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from   Constants import *   # Constants file
import random               # For random color and location

########################################################################
#                                                                      #
#                          PIXEL ARRAY CLASS                           #
#                                                                      #
########################################################################

class PixelArray:
    def __init__(self, pixelizer, screen):
        self.screen    = screen   # Main screen
        self.pixelizer = pixelizer
        self.block     = (1, 1)   # Pixel size
        self.pixels    = []

        # Set up pixel array
        self.setupPixelArray()


    # Method sets up pixel array
    def setupPixelArray(self):
        for rownum in range(self.pixelizer.getSize(ONE)): 
            for colnum in range(self.pixelizer.getSize(ZERO)):
                if not self.pixelizer.image.getpixel((colnum, rownum)):
                    self.pixels.append((colnum, rownum))
    
    # Choose random coordinate to draw pixel at
    def setCoord(self):
        x = random.randint(ZERO, SCREEN_RESOLUTION[SCREEN_WIDTH])
        y = random.randint(ZERO, SCREEN_RESOLUTION[SCREEN_HEIGHT])
        return (x, y)

    # Method chooses color of pixel
    def setColor(self):
        #  Message blue, otherwise random
        if self.coord in self.pixels:
            self.color = Colour['BLUE']
        else:
            r = random.randint(ZERO, COLOUR_MAX)
            g = random.randint(ZERO, COLOUR_MAX)
            b = random.randint(ZERO, COLOUR_MAX)
            self.color = (r, g, b)    

    # Method draws a random pixel with a random color, unless in the
    # display message.
    def drawPixel(self):
        self.coord = self.setCoord()
        self.setColor()
        self.screen.fill(self.color, (self.coord, self.block))
