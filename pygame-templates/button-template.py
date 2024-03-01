import pygame as pyg
import sys

pyg.init()
screen = pyg.display.set_mode((800,800))
pyg.display.set_caption("Buttons!")
main_font = pyg.font.SysFont("cambria", 50)


class Button():
    def __init__(self, surface, xpos, ypos, text_input) -> None:
        self.surface = surface
        self.xpos = xpos
        self.ypos = ypos
        self.rect = self.surface.get_rect(center=(self.xpos, self.ypos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.xpos, self.ypos))
        
    def update(self):
        screen.blit(self.surface, self.rect)
        screen.blit(self.text, self.text_rect)
        
        
    def changeColor(self, position):
        '''Checking color related to mouse position'''
        if position[0] in range(
            self.rect.left, self.rect.right
                ) and position[1] in range(
                    self.rect.top, 
                    self.rect.bottom):
                        self.text = main_font.render(
                        self.text_input, 
                        True, 
                        "green"
                    )
        else:
            self.text = main_font.render(
                self.text_input, 
                True, 
                "white"
            )

    def checkForInput(self, position):
        
        if position[0] in range(
    self.rect.left, self.rect.right
        ) and position[1] in range(
            self.rect.top, 
            self.rect.bottom):
            print("Button Press")


    def _update(self):
        """draw blank button and then draw message"""
        screen.blit(self.button_color, self.rect)
        screen.blit(self.msg_image, self.msg_image_rect) 
        