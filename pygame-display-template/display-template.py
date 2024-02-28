# 27 feb 2024
# I'm using 
# https://www.youtube.com/watch?v=CPWmc1otHXU
# as a basis for a very basic display setup in pygame

import pygame as pyg

pyg.init()

dsp = pyg.display.set_mode((1024, 768))
clock = pyg.time.Clock()
FPS = 60

def game() -> None:
    while True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                return
            pyg.display.update()
            clock.tick(FPS)
    
    
game()    
pyg.quit()