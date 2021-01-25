from pygame.color import Color
from random import randint

# monotone
white = Color(255,255,255)
grey = Color(122,122,122)
gray = grey
darkgrey = Color(61,61,61)
darkgray = darkgrey
lightgrey = Color(183,183,183)
lightgray = lightgrey
black = Color(0,0,0)

def random_base_grey():
    num = randint(1,254)
    return Color(num,num,num)

# reds
red = Color(255,0,0)
pink = Color(122,0,0)

def random_base_red():
    return Color(randint(0,255),0,0)

# greens
lime = Color(0,255,0)
green = Color(0,162,0)
darkGreen = Color(0,85,0)

def random_base_green():
    return Color(0,randint(0,255),0)

# blue
blue = Color(0,0,255)
cyan = Color(0,255,255)

def random_base_blue():
    return Color(0,0,randint(0,255))

# yellow
electricYellow = Color(255,255,0)

# purple
purple = Color(138,43,226)

# complex
sandy = Color(255,229,124)