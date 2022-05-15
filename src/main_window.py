import sys

from src.graphics import gameplay_graphics

sys.path.append("D:\Study\Python\Project\BabaIsYou\src")

import pygame
import os
current_dir = os.path.dirname(__file__)

from graphics import GameplayGraphics

class MainWindow():
    def __init__(self):
        pass

    def start_game(self, level):
        self.level = level
        # initialize the pygame module
        pygame.init()
        # load and set the logo
        logo = pygame.image.load(os.path.join(current_dir, "../resources/graphics/baba.png"))
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Baba Is You")
        
        # create a surface on screen 

        self.gameplay = GameplayGraphics(40,50)

        if self.level == 1:
            self.gameplay.load_map(os.path.join(current_dir,'../resources/maps/map_1.csv'),os.path.join(current_dir,'../resources/maps/map_1.info'))
        
        elif self.level == 2:
            self.gameplay.load_map(os.path.join(current_dir,'../resources/maps/map_2.csv'),os.path.join(current_dir,'../resources/maps/map_2.info'))

        self.window_width = self.gameplay.n_cols * 40
        self.window_height = self.gameplay.n_rows * 40

        self.screen = pygame.display.set_mode((self.window_width,self.window_height))


    def run_game(self):
        pass
    
    def process_event(self):
        pass

