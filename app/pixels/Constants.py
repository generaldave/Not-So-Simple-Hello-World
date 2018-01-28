'''
David Fuller

Constants file - File contains application constants.

10-15-2017
'''

from collections import namedtuple

point = namedtuple('point', ['x', 'y'])
color = namedtuple('color', ['r', 'g', 'b'])
resolution = namedtuple('resolution', ['width', 'height'])

black = color(r = 0, g = 0, b = 0)
arial_bold = 'arialbd.ttf'
font_size = 100

black_and_white = '1'

app_title = "Pixel Art"
fps = 60
