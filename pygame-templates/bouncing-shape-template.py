# 27 feb 2024
# this is continues from display template to draw a shape on to the screen    
# I'm using 
# https://www.youtube.com/watch?v=ZeCeEUF2J2c
# as a basis for a very basic display setup and line/circle draw in in pygame

import pygame as pyg

pyg.init()

dsp = pyg.display.set_mode((1024, 768)) # also known as the "surface"
clock = pyg.time.Clock()
FPS = 60

ACCELLERATION = 0.5

class Ball():
    def __init__(self) -> None:
        self.y =  200
        self.velocity = 10
    def draw(self):
#                            color = red    x and y   radius
        pyg.draw.circle(dsp, (255, 0, 0), (500, int(self.y)), 15)
        
    def move(self):
        self.velocity += ACCELLERATION
        self.y += self.velocity
        if self.y >= 401:
            self.velocity = -self.velocity 
        elif self.y == 400:
            self.velocity += ACCELLERATION
        


def game() -> None:
    ball = Ball()
    while True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                return
            if event.type == pyg.KEYDOWN and event.key == pyg.K_q:
                return
        ball.move()
            
            
            
            
            
            
            
            
            
##########################################################################            
        dsp.fill((255,255,255))
        # draw a horizontal line
        pyg.draw.line(dsp, (0, 0, 0), (0, 400), (1024, 400), 10 )

        ball.draw()
        pyg.display.update()
        clock.tick(FPS)

game()    
pyg.quit()