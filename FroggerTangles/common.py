import pygame as pyg
pyg.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize pygame and create the display surface

dsp = pyg.display.set_mode(
        (
            SCREEN_WIDTH, 
            SCREEN_HEIGHT
        )
    )


def defineColors():
    BLACK: str = '#000000'
    SILVER: str = '#C0C0C0'
    BLACK: str = '#000000'
    GREY: str = '#808080'
    GREEN: str = '#008000'
    WHITE: str = 'FFFFFF'
    BLUEISH: str = (10, 150, 240)
    
    return BLACK, SILVER, GREY, GREEN, WHITE, BLUEISH


