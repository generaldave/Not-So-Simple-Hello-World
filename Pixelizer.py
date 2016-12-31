########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Pixelizer Class: Turns text into bmp into pixels                     #
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
import pygame               # For GUI
import Image                # For creating black and white image
import ImageFont            # For setting font of image text
import ImageDraw            # For storing black and white image

########################################################################
#                                                                      #
#                           PIXELIZER CLASS                            #
#                                                                      #
########################################################################

class Pixelizer:
    def __init__(self, message):
        self.message = message   # Message to pixelize

        # Set up font
        self.font = ImageFont.truetype(ARIAL_BOLD, FONT_SIZE)
        self.size = self.font.getsize(self.message)
        self.centerText()

        # Set up bitmap
        self.drawBitmap()

    # Method returns text size
    def getSize(self, index):
        return self.size[index]

    # Method returns text image
    def getImage(self):
        return self.image

    # Method centers text
    def centerText(self):
        # Center text
        self.textX = (SCREEN_RESOLUTION[SCREEN_WIDTH]  / TWO) - \
                     (self.size[ZERO] / TWO)
        self.textY = (SCREEN_RESOLUTION[SCREEN_HEIGHT] / TWO) - \
                     (self.size[ONE]  / TWO) - \
                     FOURTEEN
        xoff       = self.size[ZERO] + self.textX
        yoff       = self.size[ONE]  + self.textY
        self.size  = (xoff, yoff)
    
    # Method draws imaginary bitmap from text
    def drawBitmap(self):
        self.image = Image.new(BLACK_AND_WHITE, self.size, BLACK)
        draw       = ImageDraw.Draw(self.image)
        draw.text((self.textX, self.textY), self.message, font = self.font)
