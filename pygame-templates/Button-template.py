# 2 March 2024
# I had started a button template from a youtube video
# that used a PNG file as the basis of that code
# I decided i didn't want to make a png-based button and to start over
# so I'm going to make a combo of the original button class from 
# alien invasion and a rectangle class derived from the pygame rectangle object
# i have to add in the display and game loop stuff for testing

# 3 march 2024:
# after many hours trying to get this work (alongside gpt) i had it mostly working
# then i asked about using pygame groups for the buttons
# and it's been is various states of not-working since then
# so I'm about to start over again

# 5 march 2024:
# I've decided to start over again
# hopefully this will be better than the last time
# --
# I did slightly better than last time but it still can't add buttons to a group() so I'm 
# giving up on GPT and writting it myself



import pygame as pyg
from pygame.sprite import Sprite

from pygame.sprite import Group
from abc import ABC, abstractmethod
#import sys


pyg.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

center_x = SCREEN_WIDTH // 2
center_y = SCREEN_HEIGHT // 2

dsp = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # also known as the "surface"
clock = pyg.time.Clock()
FPS = 60


class GameRect():
#    def __init__(self, rect, color):
#        self.rect = rect
#        self.color = color

    def __init__(self) -> None:
        super().__init__(ABC)

    @abstractmethod
    def draw(self, color, xpos, ypos, width, height ):
        self.xpos = ypos
        self.ypos = xpos
            
        self.color = color
        self.width = width
        
        self.height = height
        

        


class Button(Sprite, GameRect):
    '''
    Class for creating on screen buttons:
    rect, color, hover_color, callback
    '''
#    def _draw(self, rect, color, hover_color, callback):

    def __init__(self) -> None:
        super().__init__()
        #super().__init__(GameRect)
        #super().__init__(Sprite)
        


    def draw(self, xpos, ypos, original_color, hover_color,width, height):
        '''
        Class for drawing on screen buttons:
        x position, 
        y position, 
        initial color (three number tuple), 
        mouse over color (three number tuple)
        width: float
        height: float
        '''
        #super().__init__()
        #self.rect = rect
        #self.color = color
        self.hover_color = hover_color
        self.xpos = xpos
        self.ypos = ypos
        self.original_color = original_color
        self.width = width
        self.height = height
        self.rect = pyg.Rect(0,0, self.width, self.height)
        #self.rect.center = (center_x,center_y)
        #self.rect = xpos, ypos, width, height
        pyg.draw.rect(dsp, self.original_color, self.rect)

#    def handle_event(self, event):
#        if event.type == pyg.MOUSEBUTTONDOWN and event.button == 1:
#            if self.rect.collidepoint(event.pos):
#                self.callback()

#    def update_button(self):
#        if self.rect.collidepoint(pyg.mouse.get_pos()):
#            self.color = self.hover_color
#        else:
#            self.color = self.original_color

#    def draw(self, surface):
#        pyg.draw.rect(surface, self.color, self.rect)

###########################################


button_group = Group()

  
btnOkay = Button() #._draw(
                #pyg.Rect(100, 100, 200, 50), 
                #(0, 255, 0), 
                #(0, 200, 0), 
           # )

btnOkay_rect = btnOkay.rect

#button_group.add(button)

#all_sprites = pyg.sprite.Group(button)

button_group.add(btnOkay)

#button_group.

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
        
        for bttn in button_group:
            bttn.draw(center_x, center_y, ('#C0C0C0'), ('#B0B0B0'), 200, 50)
            #print(f"len of button group is  {len(button_group)}")
            
        
 #       button_group.draw(60, 60, ('#C0C0C0'), ('#B0B0B0'), 200, 50)
        
        
        pyg.display.flip()

        
        clock.tick(FPS)
#    pyg.quit()



game()
#pyg.quit()
#sys.exit()


''' # (save for reference)
class Button(gameRect):
    ---
    A class to build buttons for the game
    ---

    def __init__(self, ufoinv_game, msg):
        ---
        Initialize button attributes
        ---
        self.screen = ufoinv_game.screen
        self.screen_rect = self.screen.get_rect()
        
        #Set the dimensions and properties of the button 
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # The button message needs to be prepped only once
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        ---
        Turn msg into a rendered image and center text on the button
        ---
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        ---
        draw blank button and then draw message
        ---
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
'''        