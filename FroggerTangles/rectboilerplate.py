#import pygame as pyg
#from pygame.sprite import Sprite

#import importlib
#module_name = "frogger_but_blocky"
#module = importlib.import_module(module_name)

from common import Common

from abc import ABC, abstractmethod
import pygame as pyg

cmn = Common()
disp = cmn.screenInfo()

#pyg.init()
#SCREEN_WIDTH = 800
#SCREEN_HEIGHT = 600

#center_x = SCREEN_WIDTH // 2
#center_y = SCREEN_HEIGHT // 2

#BLACK: str = '#000000'

#dsp = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # also known as the "surface"
#clock = pyg.time.Clock()
#FPS = 60

class GameRect(ABC):
    '''A very generic shape Rectangle'''
    
    def __init__(self, xpos, ypos, width, height, color) -> None:
        self.xpos, self.ypos = xpos, ypos
        self.width = width
        self.height = height
        self.color = color
    
    def draw_rect(self):
        rect = pyg.Rect(self.xpos, self.ypos, self.width, self.height)
        pyg.draw.rect(disp, self.color, rect)
        
        return rect
    
    @abstractmethod
    def draw(self):
        pass
        
'''        
#class Button(GameRect, Sprite):
#    def __init__(self, xpos, ypos, width, height, original_color, hover_color) -> None:    

#        Button class: generic class for any necessary buttons

        super().__init__(xpos, ypos, width, height, original_color)
        Sprite.__init__(self)  # Initialize Sprite class

        self.pressed = False # YT video made argument this is necessary
        self.hover_color = hover_color
        self.original_color = original_color
        self.cur_color = original_color
        
        xpos = (SCREEN_WIDTH - width) // 2
        ypos = (SCREEN_HEIGHT - height) // 2
    
    def draw(self, caption, text_color=BLACK,  font=None):

#        Drawing the button: unique text for each button

        self.font = font   
        self.caption = caption     
        self.rect = self.draw_rect()
        

        self.prepCaption(caption, self.rect,text_color, 30)
        self.check_click(self.rect)
        self.check_hover(self.rect)
        
    def prepCaption(self, caption, rect, text_color, text_size):

#        Creating the font object, text surface and text rectangle
#        then blitting it to the screen/window

        font_obj = pyg.font.Font(self.font, text_size)
        text_surface = font_obj.render(caption, True, text_color, self.original_color)
        text_rect = text_surface.get_rect(center=rect.center)
        dsp.blit(text_surface,text_rect)
        
    def check_click(self, rect):

#        Registering the left mouse button click

        mouse_pos = pyg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):

            if pyg.mouse.get_pressed()[0]:
                self.pressed = True
            else:
                if self.pressed:
                    print("mouse released")
                    self.pressed = False

    def check_hover(self, rect):

#        Registering a mouse hover-over

        mouse_pos = pyg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.original_color = self.hover_color

        elif not self.rect.collidepoint(mouse_pos):
            self.original_color = self.cur_color
'''