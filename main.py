import pygame as pg
pg.init()

import classes

WINDOWHEIGHT = 600
WINDOWWIDTH = 800

def close():
    pg.quit()
    quit()

def main():
    win = pg.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    pg.display.set_caption('Open World')

    clock = pg.time.Clock()

    player = classes.Player()

    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                close()
    
        # render everything
        win.fill((0,0,0))

        player.render(win)

        pg.display.flip()

        clock.tick()

if __name__ == '__main__':
    main()