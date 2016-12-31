########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# init class: App initializer                                          #
#                                                                      #
# Created on 2016-12-30                                                #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from   Constants  import *   # Constants file
from   Pixelizer  import *   # Pixelizer Class
from   PixelArray import *   # PixelArray Class
import pygame                # For GUI

########################################################################
#                                                                      #
#                              INIT CLASS                              #
#                                                                      #
########################################################################

class init:
    def __init__(self, appDirectory):
        self.appDirectory = appDirectory

        # Set up GUI
        self.setupGUI()

        # Set up pixel objects
        self.setupObjects()

        # Run app
        self.runApp()

    # Mehtod sets up GUI
    def setupGUI(self):
        # Screen attributes
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_RESOLUTION)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()   # For frames per second

    # Method sets up pixel objects
    def setupObjects(self):
        pixelizer = Pixelizer("Hello World")
        self.pixelArray = PixelArray(pixelizer, self.screen)

    # Method runs app
    def runApp(self):
        running = True
        while running:
            for event in pygame.event.get():
                # Handle quit event
                if event.type == pygame.QUIT:
                    running = False

            # Draw pixel
            self.pixelArray.drawPixel()

            # Update Screen
            pygame.display.update()
            self.clock.tick(FPS)            

        # Close app cleanly
        pygame.quit()
