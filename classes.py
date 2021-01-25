from pygame.image import load as getImg
class Player:
    def __init__(self):
        self.coords = [400,300]
        self.sprite = getImg('assets/player/playerPlaceholderBase.png')
    def render(self,surf):
        surf.blit(self.sprite,self.coords)