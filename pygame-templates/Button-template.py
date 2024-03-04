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


import pygame as pyg
from pygame.sprite import Group
from abc import ABC, abstractmethod
import sys

pyg.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

dsp = pyg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # also known as the "surface"
clock = pyg.time.Clock()
FPS = 60

  
    


# Usage example:
# screen_rect = ScreenUtils.get_screen_rect(self.screen)

'''
What I would "really" like to do is create a generic rectangle class that derives from the pygame
rectangle that derive any/all recangles as needed from that generic one

my generic one derived from the pygame one would have extra parameters beyone the default
the defaulting being:
x coords
y coords
width
height

Beyond that, I want to pass in the bg color at least
for this derived button rectangle I would likely want to put in things like the font type and size
unless those could be defined as variables after instantiating the object...

I'll find out as I go along
first step: create generic rectangle
'''

class GameRect(ABC):
    '''
    A generic rectangle from which all game rectangles will be derived
    (name subject to change)
    '''

    def __init__(self, xpos: int, ypos: int, width: int, height: int, color: pyg.Color,
                 draw_border: bool = True, border_width: int = 2, border_color: pyg.Color = (0, 0, 0)) -> None:
        self.rect = pyg.Rect(xpos, ypos, width, height)
        self.color = color
        self.draw_border = draw_border
        self.border_width = border_width
        self.border_color = border_color

    @abstractmethod
    def _draw(self, surface: pyg.Surface) -> None:
        '''
        Draw the rectangle on the specified surface.
        This method should be implemented by subclasses.
        '''
        pass





class Button(pyg.sprite.Sprite):
    def __init__(self, xpos: int, ypos: int, width: int, height: int, color: pyg.Color, caption: str,
                 font: pyg.font.Font, surface: pyg.Surface) -> None:
        super().__init__()
        self.image = pyg.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (xpos, ypos)
        self.color = color
        self.caption = caption
        self.font = font
        self.mouse_over = False
        self.draw(surface)  # Draw the button initially on the provided surface

    def draw(self, surface: pyg.Surface) -> None:
        # Draw the button rectangle
        self.image.fill(self.color)
        pyg.draw.rect(self.image, pyg.Color('black'), self.rect, 2)  # Draw the border
        if self.caption:
            text_surface = self.font.render(self.caption, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=self.rect.center)
            self.image.blit(text_surface, text_rect)

        # Draw the button onto the provided surface
        surface.blit(self.image, self.rect.topleft)

    def on_mouse_over(self, surface: pyg.Surface) -> None:
        if self.rect.collidepoint(pyg.mouse.get_pos()):  # Check if mouse is over the button
            self.color = pyg.Color('gray')
        else:
            self.color = pyg.Color('#c0c0c0')  # Reset to default color
        self.draw(surface)  # Redraw the button with updated color

    def on_click(self) -> None:
        if self.caption == "Quit":
            pyg.quit()


            
            
            
        
ButtonGroup = Group()


#getScreenRect = getSurfaceRect()
#screenRect = getScreenRect.getRectSurface(dsp)

#print(f"getScreenRect width is {getScreenRect.width}")

buttonFont = pyg.font.Font(None, 36)

okButton = Button(SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2 - 37, 150, 75, pyg.Color('#c0c0c0'), "OK", buttonFont, dsp)
ButtonGroup.add(okButton)

quitButton = Button(SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2 + 100, 150, 75, pyg.Color('#c0c0c0'), "Quit", buttonFont, dsp)
ButtonGroup.add(quitButton)


#GenButton = Button()












#okButton = Button(0,0, 150, 75, '#c0c0c0',"OK", buttonFont,True,2,'#000000')
#ButtonGroup.add(okButton)
#okButton.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

#quitButton = Button(1,1, 150, 75, '#c0c0c0',"Quit", buttonFont,True,2,'#000000')
#ButtonGroup.add(quitButton)
#quitButton.center = (SCREEN_WIDTH // 2, (SCREEN_HEIGHT // 2 + (quitButton.height + 30) ) )
#quitButton.top = okButton.bottom + 30


#ButtonGroup.update()


#okButton._draw(dsp)

###########################################

def game() -> None:
    while True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                return
            elif event.type == pyg.KEYDOWN and event.key == pyg.K_q:
                pyg.quit()
                return
            elif event.type == pyg.MOUSEMOTION:
                for button in ButtonGroup:
                    button.on_mouse_over(dsp)  # Pass dsp to on_mouse_over()
            elif event.type == pyg.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    for button in ButtonGroup:
                        if button.rect.collidepoint(event.pos):
                            button.on_click()

        dsp.fill((255, 255, 255))
        ButtonGroup.draw(dsp)
        pyg.display.update()
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