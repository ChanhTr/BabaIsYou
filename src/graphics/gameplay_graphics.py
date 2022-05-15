import sys

sys.path.append("D:\Study\Python\Project\BabaIsYou\src")

import pygame
import os
import numpy as np
import pandas as pd
from graphics.object_graphics import *
from gameplay import Gameplay, Tile

class GameplayGraphics(Gameplay):
    def load_map(self, map_file, info_file):
        self.map_file = map_file
        self.info_file = info_file
        with open(info_file) as f:
            self.n_rows = int(f.readline())
            self.n_cols = int(f.readline())
        self.rules = []
        self.tiles = np.zeros((self.n_rows, self.n_cols), dtype=Tile) #reset va resize cho vua info file
        for i in range(self.n_rows):
            for j in range(self.n_cols):
                self.tiles[i,j] = Tile() 
        map_data = pd.read_csv(map_file, header = None, sep = ';')
        map_array = np.array(map_data, dtype = str)
        for r in range(self.n_rows):
            for c in range(self.n_cols):
                value_data = map_array[r,c].split('/')
                for value in value_data:
                    if value == '':
                        continue
                    elif value == 'baba':
                        self.tiles[r,c].add_object(BabaGraphic())
                    elif value == 'rock':
                        self.tiles[r,c].add_object(RockGraphic())
                    elif value == 'water':
                        self.tiles[r,c].add_object(WaterGraphic())
                    elif value == 'skull':
                        self.tiles[r,c].add_object(SkullGraphic())
                    elif value == 'wall':
                        self.tiles[r,c].add_object(WallGraphic())
                    elif value == 'flag':
                        self.tiles[r,c].add_object(FlagGraphic())
                    elif value.isupper():
                        self.tiles[r,c].add_object(WordGraphic(value.lower()))

    def render(self, window):
        # window.set_mode((41*self.n_cols,41*self.n_rows))
        for r in range(self.n_rows):
            for c in range(self.n_cols):
                tile = self.tiles[r,c]
                for obj in tile.objects:
                    obj.render(window, 40*c, 40*r)

if __name__ == '__main__':
        # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/baba.png"))
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Baba Is You")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((1170,800), pygame.RESIZABLE)

    # define a variable to control the main loop
    running = True

    # main loop
    gameplaygraphics_test = GameplayGraphics(40, 50)
    gameplaygraphics_test.load_map(os.path.join(current_dir,'../../resources/maps/map_2.csv'),os.path.join(current_dir,'../../resources/maps/map_2.info'))


    while running:
    
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                print('bye')
                running = False
        
        gameplaygraphics_test.render(screen)

        pygame.display.update()
