'''
Test room for new features
'''
from pygame.surface import Surface

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
        'deserts',
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
                surface.blit(TestTile.tiles[self.map.type])

class TestTile:
    pass