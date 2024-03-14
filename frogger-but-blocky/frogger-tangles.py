# attempt to make some kind of version of the very blocky version of frogger
# written by TheCodingTrain in JS/p5.js
# then re-factored in video
# https://www.youtube.com/watch?v=c6WdJltqEtM
# 29 Feb 2024 (it's a leap year)
# the GetWindowRect class is supposed to be an attempt to get a rectangle derived from the game screen much easier and universal
# included below (until I move it) is a generic shape class followed by a rectangle class derived from the shape class



import pygame as pyg
from pygame.sprite import Sprite, Group

from abc import ABC, abstractmethod

pyg.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

center_x = SCREEN_WIDTH // 2
center_y = SCREEN_HEIGHT // 2

SILVER: str = '#C0C0C0'
BLACK: str = '#000000'
GREY: str = '#808080'
GREEN: str = '#008000'
WHITE: str = 'FFFFFF'



dsp = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # also known as the "surface"
clock = pyg.time.Clock()
FPS = 60

class GameRect(ABC):
    '''A very generic shape Rectangle'''

    def __init__(self, xpos, ypos, width, height, original_color) -> None:
        self.xpos, self.ypos = xpos, ypos
        self.width = width
        self.height = height
        self.original_color = original_color
    
    def draw_rect(self):
        self.rect = pyg.Rect(self.xpos, self.ypos, self.width, self.height)
        self.rect.centerx = self.xpos
        self.rect.centery = self.ypos
        pyg.draw.rect(dsp, self.original_color, self.rect)
        
        return self.rect
    
    @abstractmethod
    def draw(self):
        pass
    

def game() -> None:
    while True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                    pyg.quit()
                    return
            elif event.type == pyg.KEYDOWN and event.key == pyg.K_q:
                pyg.quit()
                return

        dsp.fill((255, 255, 255))



        pyg.display.flip()
        
        clock.tick(FPS)

game()
