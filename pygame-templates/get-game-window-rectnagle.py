# 29 feb 2024 (it's leap year)
# after realizing i was gonig to need to get the dimensions of the screen for i think every project
# well really "get the rectangle of" the game window
# and that the "alien invasion" game fromt he crash book used that duplicate code over and and over again,
# I decided it would be a good addition to this boiler plate
# also, I got it from chatgpt (the free one)


'''
pygame pre-defines

x,y
top, left, bottom, right
topleft, bottomleft, topright, bottomright
midtop, midleft, midbottom, midright
center, centerx, centery
size, width, height
w,h

GPT had further explanation for this class:

Explanation:

pygame.Surface: Represents an in-memory surface used for drawing.

cls: In a class method, cls refers to the class itself (similar to how self refers to the instance in instance methods). It allows you to access class-level attributes and methods.

screen: This parameter represents the Pygame display surface, which is typically created using pygame.display.set_mode(). It's an instance of pygame.

Surface that represents the game window.

get_screen_rect(): This class method of ScreenUtils takes a screen parameter, retrieves the rectangle of the Pygame display surface using screen.get_rect(), and returns it.

Example usage: In the main() function, we initialize Pygame, create a display surface (screen), call ScreenUtils.get_screen_rect(screen) to get the screen rectangle,
 and then access various attributes of the screen rectangle to demonstrate its usage.
This script demonstrates how to use the ScreenUtils class to retrieve and work with the rectangle of the Pygame display surface.


'''


import pygame

class GetWindowRect:
    @classmethod
    def get_screen_rect(cls, screen):
        """
        Get the rectangle of the Pygame display surface.

        Parameters:
            screen (pygame.Surface): The Pygame display surface.

        Returns:
            pygame.Rect: A rectangle representing the Pygame display surface.
        
        example:
            screen = pygame.display.set_mode((screen_width, screen_height))
            screen_rect = ScreenUtils.get_screen_rect(screen)
            print("Screen width:", screen_rect.width)
            print("Screen height:", screen_rect.height)

        Reminder for rectangles:
            x,y
            top, left, bottom, right
            topleft, bottomleft, topright, bottomright
            midtop, midleft, midbottom, midright
            center, centerx, centery
            size, width, height
            w,h    

        """
        return screen.get_rect()

# Example usage:
def main():
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    # Retrieve the rectangle of the screen using ScreenUtils
    screen_rect = GetWindowRect.get_screen_rect(screen)

    # Access attributes of the screen rectangle
    print("Screen width:", screen_rect.width)
    print("Screen height:", screen_rect.height)
    print("Screen top-left corner:", screen_rect.topleft)
    print("Screen center:", screen_rect.center)

if __name__ == "__main__":
    main()
