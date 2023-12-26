# python crashcourse book I bought for some reason
# 26 Dec 2023
# I skipped to chapter 12 because i know most of the prior stuff (probably)

# i tried to install pygame, complained then said pip needed to upgrade, 
# tried to upgrade pip and it some how forgot pip existed (screwed up path?)
# attempted to fix with chocolatey - ended up upgrading python to 3.12.1 x64
# used these two lines to re-acknolwedge paths
#  Import-Module $env:ChocolateyInstall\helpers\chocolateyProfile.psm1
# refreshenv
# finally upgraded pip and installed pygame. took a while. also set vscode to 3.12. 
# which I assume it will forget

import sys, pygame

class AlienInvasion:
    # overall class to manage assets and behaviors etc

    def __init__(self):
        # initialize game and create resources
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
    
    def run_game(self):
        # start game loop
        while True:
            # watch for kb and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()

if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()


