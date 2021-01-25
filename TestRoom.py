'''
Test room for new features
I dont know why its oop, but i started it that way and am keeping it that way
At least it makes a clear distinction between this file and the main file
'''
import pygame as pg
from pygame.surface import Surface
import classes
from color import *
pg.init()

class TestMap:
    '''
    Current Settings:
    '''
    tileSize = 50
    chunkHeight = 16 # in tiles
    chunkWidth = 16 # in tiles
    mapHeight = 16 # in chunks
    mapWidth = 16 # in chunks
    '''
    Map Type Bindings:
    '''
    biomeBinds = [
        'plains',
        'desert',
        'lake',
        'purple-land'
    ]
    def __init__(self,type):
        self.type = type

class TestChunkHandler:
    def __init__(self,map):
        self.map = map
        self.chunks = []
    def load_chunk(self,x,y):
        chunkSprite = Surface(TestMap.tileSize,TestMap.tileSize)
        for y in range(TestMap.chunkHeight):
            for x in range(TestMap.chunkWidth):
                chunkSprite.blit(TestTile.tiles[self.map.type])

class TestTile:
    plains = Surface(TestMap.tileSize,TestMap.tileSize)
    desert = Surface(TestMap.tileSize,TestMap.tileSize)
    lake = Surface(TestMap.tileSize,TestMap.tileSize)
    purpleland = Surface(TestMap.tileSize,TestMap.tileSize)

    plains.fill(lime)
    desert.fill(sandy)
    lake.fill(blue)
    purpleland.fill(purple)

    tiles = {
        'plains' : plains,
        'desert' : desert,
        'lake' : lake,
        'purple-land' : purpleland,
    }

class TestRun:
    # like seriously, this should be functional, not oop
    # but gotta keep the style going
    
    binds = {
        'up' : 'w',
        'down' : 's',
        'left' : 'a',
        'right' : 'd'
    }

    wHeight = 600
    wWidth = 800

    xSpeed = 5
    ySpeed = 5
    
    def __init__(self):
        self.win = pg.display.set_mode((TestRun.wWidth,TestRun.wHeight))
        self.player = classes.Player()
        self.map = TestMap('plains')
    
    def close(self):
        pg.quit()
        quit()

    def run(self):
        done = False
        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.close()
            
            keys = pg.key.get_pressed()

            if keys[TestRun.binds['up']]:
                self.player.vel[1] += TestRun.ySpeed
            
            elif keys[TestRun.binds['down']]:
                self.player.vel[1] -= TestRun.ySpeed 


if __name__ == '__main__':
    # ewwww i hate code like this
    app = TestRun()
    app.run()
