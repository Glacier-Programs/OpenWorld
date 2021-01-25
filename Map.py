from pygame.color import Color
from random import randint

class Chunk:
    def __init__(self):
        pass

class MapGenerator:
    def __init__(self,biomeSize):
        # biomesize is radius, so half width of biome
        spot1 = (randint(biomeSize,worldsize-biomesize),randint(biomeSize,worldsize-biomesize))

class Map:
    def __init__(self,biomeSpots,width,height):
        self.biomeSpots = biomeSpots
        self.width = width
        self.height = height