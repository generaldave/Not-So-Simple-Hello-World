'''
David Fuller

Constants file - File contains application constants.

10-15-2017
'''

from collections import namedtuple

point = namedtuple('point', ['x', 'y'])
color = namedtuple('color', ['r', 'g', 'b'])
resolution = namedtuple('resolution', ['width', 'height'])

background_color = color(r = 127, g = 127, b = 127)
screen_resolution = resolution(width = 640, height = 200)

app_title = "Pixel Art"
fps = 60
