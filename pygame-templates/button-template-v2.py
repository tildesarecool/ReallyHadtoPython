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


dsp = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # also known as the "surface"
clock = pyg.time.Clock()
FPS = 60

class GameRect(ABC):
    '''A very generic shape Rectangle'''

    def __init__(self, xpos, ypos, width, height, original_color) -> None:
        #self.xpos = xpos 
        #self.ypos = ypos
        self.xpos, self.ypos = xpos, ypos
        self.width = width
        self.height = height
        self.original_color = original_color
    
    def draw_rect(self):
        rect = pyg.Rect(self.xpos, self.ypos, self.width, self.height)
        rect.centerx = self.xpos
        rect.centery = self.ypos
        pyg.draw.rect(dsp, self.original_color, rect)
        
        return rect
    
    @abstractmethod
    def draw(self):
        pass
        
        
class Button(GameRect, Sprite):
    def __init__(self, xpos, ypos, width, height, original_color, hover_color=GREY) -> None:    
        super().__init__(xpos, ypos, width, height, original_color)
        Sprite.__init__(self)  # Initialize Sprite class

        self.hover_color = hover_color
        self.original_color = original_color
        self.cur_color = self.original_color
        
        xpos = (SCREEN_WIDTH - width) // 2
        ypos = (SCREEN_HEIGHT - height) // 2
        


    
    def draw(self, caption, text_color=BLACK,  font=None):
        self.font = font   
        self.caption = caption     
        rect = self.draw_rect()

        self.prepCaption(caption, rect,text_color, 30)
        self.check_click(rect)
        
    def prepCaption(self, caption, rect, text_color, text_size):
#        self.caption = caption
        #rect = self.draw_rect()
        font_obj = pyg.font.Font(self.font, text_size)
        text_surface = font_obj.render(caption, True, text_color, self.original_color)
        text_rect = text_surface.get_rect(center=rect.center)
        dsp.blit(text_surface,text_rect)
        
    def check_click(self, rect):
        mouse_pos = pyg.mouse.get_pos()
        #if self.top_rect.collidepoint(mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            #self.hover_color = '#D74B4B'
            self.cur_color == self.hover_color
            print("collide")
            #if pyg.mouse.get_pressed()[0]:
            if pyg.MOUSEBUTTONUP == 0:
#                self.dynamic_elevation = 0
                self.pressed = True
                print("mouse released")
            else:
 #               self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    print('click')
                    self.pressed = False
                    
        else:
#            self.dynamic_elevation = self.elevation
            #self.hover_color = '#475F77'
            self.cur_color = self.original_color
        
        
    
btnGroup = Group()


okButton = Button(center_x, center_y + 10, 150, 50, SILVER)
#btnGroup.add(okButton)
okButton.ypos -= (okButton.height * 2)

cancelButton = Button(
    okButton.xpos, 
    okButton.ypos + 100, 
    okButton.width, 
    okButton.height, 
    #'#008000',
    okButton.original_color, 
    okButton.hover_color 
    )

btnGroup.add(okButton, cancelButton)


#getOkbtnYpos = okButton.ypos
#print(f"ok button y pos is {getOkbtnYpos}")

#okButton.draw_rect().center = (center_x, center_y)
#okButton.ypos = center_y

#okButton.draw_rect().center = (center_x,center_y)

#okButton.draw()
#okButton.test_values()

#newRect.draw(('#C0C0C0'), 0,0, 150, 50)

#newRect.rect.center = (center_x, center_y)

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
        #button_group.draw(dsp)
        
        okButton.draw("Okay", (BLACK),  None)
        cancelButton.draw("Cancel",(BLACK),  None)
        #okButton.draw("Arial")
        #okButton.prepCaption()


#        for bttn in button_group:
#            bttn.draw(center_x, center_y, ('#C0C0C0'), ('#B0B0B0'), 200, 50)
            #print(f"len of button group is  {len(button_group)}")
            
        
 #       button_group.draw(60, 60, ('#C0C0C0'), ('#B0B0B0'), 200, 50)
        
        
        pyg.display.flip()

        
        clock.tick(FPS)
    
    
    
    
game()