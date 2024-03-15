# attempt to make some kind of version of the very blocky version of frogger
# written by TheCodingTrain in JS/p5.js
# then re-factored in video
# https://www.youtube.com/watch?v=c6WdJltqEtM
# 29 Feb 2024 (it's a leap year)

BLACK: str = '#000000'
SILVER: str = '#C0C0C0'
BLACK: str = '#000000'
GREY: str = '#808080'
GREEN: str = '#008000'
WHITE: str = 'FFFFFF'

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

import pygame as pyg

from pygame.sprite import Group

#import frog
from frog import Frog

pyg.init()


center_x = SCREEN_WIDTH // 2
center_y = SCREEN_HEIGHT // 2

dsp = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # also known as the "surface"
clock = pyg.time.Clock()
FPS = 60

froggie = Frog(500,500,100,100,GREEN)
#frogger = Frog(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 10, 100,  100, GREEN)

def game() -> None:
    while True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                    pyg.quit()
                    return
            elif event.type == pyg.KEYDOWN and event.key == pyg.K_q:
                pyg.quit()
                return
        dsp.fill((10, 150, 240))
        #dsp.fill('#00000080')


 #       frogger.draw()
        froggie.draw()


        pyg.display.flip()        
        clock.tick(FPS)

game()
