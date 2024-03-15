import pygame as pyg
#from pygame.sprite import Group
#from pygame.sprite import Sprite



pyg.init()

dsp = pyg.display.set_mode((1000, 800)) 
clock = pyg.time.Clock()
FPS = 60

def drawRect():
    
    #self.xpos, self.ypos = xpos, ypos
    #self.y = ypos
    #self.color = color
    #self.width = width
    #self.height = height
    
    #pyg.Rect(xpos,ypos,width, height)
    rect = pyg.Rect(100, 100, 250,250)
    pyg.draw.rect(dsp, '#808080', rect )
    
    rect = pyg.Rect(105, 105, 230,230)
    pyg.draw.rect(dsp, '#C0C0C0', rect )
    

def game() -> None:
    
    while True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                return
            if event.type == pyg.KEYDOWN and event.key == pyg.K_q:
                return           
##########################################################################            
        dsp.fill((255,255,255))

        drawRect()
        
        pyg.display.update()
        clock.tick(FPS)

game()    