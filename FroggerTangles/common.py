import pygame as pyg
pyg.init()

# Initialize pygame and create the display surface

class Common():
    '''Command variables and settings'''
    def __init__(self):

        self.BLACK: str = '#000000'
        self.SILVER: str = '#C0C0C0'
        self.BLACK: str = '#000000'
        self.GREY: str = '#808080'
        self.GREEN: str = '#008000'
        self.WHITE: str = '#FFFFFF'
        self.BLUEISH: str = (10, 150, 240)
        
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        
        self.cellWidth = 50
        self.cellHeight = 50

    def screenInfo(self):
        self.dsp = pyg.display.set_mode(
                (
                    self.SCREEN_WIDTH, 
                    self.SCREEN_HEIGHT
                )
            )
        return self.dsp
    
