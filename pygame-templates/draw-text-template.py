# 27 feb 2024
# this is continues from display template to draw some text to the screen    
# I'm using 
# https://www.youtube.com/watch?v=cGrOr5V0iqw
# as a basis for a very basic display text to screen template

import pygame as pyg

pyg.init()

dsp = pyg.display.set_mode((1024, 768)) # also known as the "surface"
clock = pyg.time.Clock()
FPS = 60

def print_text(text, position, font_size) -> None:
#                              fontface     size  bold? Italics? 
    font = pyg.font.SysFont("Times New Roman", font_size, True, False)
#                            "text"     anti-alias? set rgb
    surface = font.render(text, True, (255,0,0))
    dsp.blit(surface, position)


def game() -> None:
    while True:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                return
            if event.type == pyg.KEYDOWN and event.key == pyg.K_q:
                return
        cur_fps = clock.get_fps()
        cur_fps_fs = str(cur_fps).format( "{cur_fps:.2f} ")
        #cur_fps_fl = float(cur_fps_fs)
            
##########################################################################            
        dsp.fill((255,255,255))
        
        #cur_fps = f"{cur_fps:.2f}"
        some_float = 1234.03402034923485
        #rand_string = f"my name is {cur_fps_fl}"
        #print_text(rand_string, (200,200), 30)
        print_text("hello", (300,250), 50)
        
        print_text(cur_fps_fs, (10,50), 10)
        

        pyg.display.update()
        clock.tick(FPS)

game()    
pyg.quit()