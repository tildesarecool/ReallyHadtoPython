# 29 feb 2024 (it's leap year)
# after realizing i was gonig to need to get the dimensios of the screen for i think every project
# and that the "alien invasion" game fromt he crash book used that duplicate code over and and over again,
# I decided it would be a good addition to this boiler plate
# also, I got it from chatgpt (the free one)

import pygame as pyg

pyg.init()

dsp = pyg.display.set_mode(
    (
        1024, 
        768
    )
)
clock = pyg.time.Clock()
FPS = 60



class ScreenUtils:
    '''Method get_screen_size takes in created surface and returns x and y of screen '''
    # see the separate screen utils file for better explanation
    @staticmethod
    def get_screen_size(screen):
        """Get the width and height of the Pygame display surface."""
        return screen.get_width(), screen.get_height()

# Usage example:
width, height = ScreenUtils.get_screen_size(dsp)
print(f"The width of the screen is {width} and the height is {height}")

def game() -> None:
    print(f"game window size is {ScreenUtils.get_screen_size(dsp)}")
    while True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                return
            if event.type == pyg.KEYDOWN and event.key == pyg.K_q:
                return
            
            

            
            
            
##########################################################################            
        dsp.fill((255,255,255))
        # draw a horizontal line
        pyg.draw.line(dsp, (0, 0, 0), (0, 400), (1024, 400), 10 )

        pyg.display.update()
        clock.tick(FPS)
    
    
game()    
pyg.quit()