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
# 
# 



import pygame as pyg
from pygame.sprite import Sprite

from pygame.sprite import Group
from abc import ABC, abstractmethod
import sys

class Rectangle:
    def __init__(self, rect, color):
        self.rect = rect
        self.color = color

    def draw(self, surface):
        pyg.draw.rect(surface, self.color, self.rect)

class Button(Rectangle):
    '''
    Class for creating on screen buttons:
    rect, color, hover_color, callback
    '''
    def __init__(self, rect, color, hover_color, callback):
        super().__init__(rect, color)
        self.hover_color = hover_color
        self.callback = callback
        self.original_color = color

    def handle_event(self, event):
        if event.type == pyg.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.callback()

    def update(self):
        if self.rect.collidepoint(pyg.mouse.get_pos()):
            self.color = self.hover_color
        else:
            self.color = self.original_color


###########################################
pyg.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

dsp = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # also known as the "surface"
clock = pyg.time.Clock()
FPS = 60

  
button = Button(pyg.Rect(100, 100, 200, 50), (0, 255, 0), (0, 200, 0), lambda: print("Button clicked"))


#all_sprites = pyg.sprite.Group(button)


def game() -> None:
    while True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                    pyg.quit()
                    return
            elif event.type == pyg.KEYDOWN and event.key == pyg.K_q:
                pyg.quit()
                return
            button.handle_event(event)

        button.update()
        dsp.fill((255, 255, 255))
        
#        all_sprites.update()
#        all_sprites.draw(dsp)
        
        button.draw(dsp)
        
        pyg.display.flip()

        
        clock.tick(FPS)



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