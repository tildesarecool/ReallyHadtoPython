# attempt to make some kind of version of the very blocky version of frogger
# written by TheCodingTrain in JS/p5.js
# then re-factored in video
# https://www.youtube.com/watch?v=c6WdJltqEtM
# 29 Feb 2024 (it's a leap year)

#from common import dsp
#from common import SCREEN_WIDTH, SCREEN_HEIGHT
from common import Common 

cmn = Common()


import pygame as pyg
from time import sleep



disp = cmn.screenInfo()
#SCREEN_WIDTH = 800
#SCREEN_HEIGHT = 600

#import pygame as pyg

from pygame.sprite import Group

#import frog
from frog import Frog
from lanes import Lane
from cars import Car

pyg.init()


center_x = cmn.SCREEN_WIDTH / 2
center_y = cmn.SCREEN_HEIGHT / 2

#dsp = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # also known as the "surface"
clock = pyg.time.Clock()
FPS = 60

froggie = Frog(cmn.SCREEN_WIDTH // 2, cmn.SCREEN_HEIGHT - 55, cmn.cellWidth, cmn.cellHeight, cmn.GREEN)
#frogger = Frog(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 10, 100,  100, GREEN)

laneOne = Lane(
    0, 
    cmn.SCREEN_HEIGHT - (froggie.height * 6) - 20, 
    cmn.SCREEN_WIDTH, 
    froggie.height * 5, 
    cmn.SILVER
    )

sidewalkOne = Lane(
    0,
    #laneOne.draw_rect().top,
    #cmn.SCREEN_HEIGHT - (froggie.height * 8) ,
    laneOne.height - 45,
    cmn.SCREEN_WIDTH,
    froggie.height * 1.5,
    cmn.GREY
    )

EndZone = Lane(
    0,
    #laneOne.draw_rect().top,
    #cmn.SCREEN_HEIGHT - (froggie.height * 8) ,
    0,
    cmn.SCREEN_WIDTH,
    froggie.height * 1.5,
    cmn.GREEN
    )


carsGroup = Group()

regCar = Car(
    0,
    0,
    froggie.width * 2, 
    froggie.height,
    cmn.WHITE
    )




regBus = Car(
    0,
    0,
    froggie.width * 3, 
    froggie.height,
    cmn.BLACK
    )



#regBus.xpos = regCar.xpos - 60



carsGroup.add(regCar)#, regBus)

def addTraffic():
    #carsGroup.draw(disp)
    regCarRect = regCar.draw_rect()
    #regCarRect.y = regCar.ypos
    #regCarRect.x = regCar.xpos
    
    regCarRect.y = cmn.SCREEN_HEIGHT - (froggie.height * 6) - 20
    #regCarRect.x = cmn.SCREEN_WIDTH
    
#    regCar.ypos = laneOne.ypos + 5
#    regCar.xpos = cmn.SCREEN_WIDTH - 5

    regCar.ypos = regCarRect.y
    #regCar.xpos = regCarRect.x

    
    regCar.draw()    
###################################################
    regBusRect = regCar.draw_rect()
    regBusRect.y = regCarRect.y
    regBus.ypos = regBusRect.y
    regBus.xpos = regCarRect.x + (regCarRect.width + 50)
    regBus.draw()
    #regBusRect.right = regCarRect.width - 200
    #regBus.ypos = regCar.ypos
    
    
#    for v in carsGroup:

#        v.draw()
    

def game() -> None:
    while True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                    pyg.quit()
                    return
            elif event.type == pyg.KEYDOWN and event.key == pyg.K_q:
                pyg.quit()
                return
        #dsp.fill((10, 150, 240))
        disp.fill(cmn.BLUEISH)
        #dsp.fill('#00000080')
        sidewalkOne.draw()
        laneOne.draw()
        EndZone.draw()
        
        addTraffic()
        
        #regCar.draw()
        #regBus.draw()
        

        froggie.update()
        
        froggie.draw()
        


        pyg.display.flip()        
        clock.tick(FPS)

game()
