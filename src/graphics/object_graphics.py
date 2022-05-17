import sys
sys.path.append("D:\Study\Python\Project\BabaIsYou\src")

from gameplay import Baba, Rock, Water, Wall, Flag, Skull, Word
import pygame
import os
current_dir = os.path.dirname(__file__)

class BabaGraphic(Baba):
    def render(self, window, x, y):
        baba_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/baba.png"))
        # baba_resized = pygame.transform.scale(baba_image,(baba_image.get_width()/6, baba_image.get_height()/6))
        baba_resized = pygame.transform.scale(baba_image,(40,40))
        window.blit(baba_resized,[x,y])
        

class RockGraphic(Rock):
    def render(self, window, x, y):
        rock_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/rock.png"))
        rock_resized = pygame.transform.scale(rock_image,(40,40))
        window.blit(rock_resized,[x,y])
        

class WaterGraphic(Water):
    def render(self, window, x, y):
        water_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/water.png"))
        water_resized = pygame.transform.scale(water_image,(40,40))
        window.blit(water_resized,[x,y])
        

class WallGraphic(Wall):
    def render(self, window, x, y):
        wall_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/wall.png"))
        wall_resized = pygame.transform.scale(wall_image,(40,40))
        window.blit(wall_resized,[x,y])
        

class FlagGraphic(Flag):
    def render(self, window, x, y):
        flag_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/flag.png"))
        flag_resized = pygame.transform.scale(flag_image,(40,40))
        window.blit(flag_resized,[x,y])
        

class SkullGraphic(Skull):
    def render(self, window, x, y):
        skull_image = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/skull.png"))
        skull_resized = pygame.transform.scale(skull_image,(40,40))
        window.blit(skull_resized,[x,y])
        

class WordGraphic(Word):
    def render(self, window, x, y):
        png_file_name = "../../resources/graphics/" + self.value.upper() + "-w.png"
        png_image = pygame.image.load(os.path.join(current_dir, png_file_name))
        png_image_resized = pygame.transform.scale(png_image,(40,40))
        window.blit(png_image_resized, [x,y])


if __name__ == '__main__':
        # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load(os.path.join(current_dir, "../../resources/graphics/baba.png"))
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Baba Is You")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((960,720), pygame.RESIZABLE)
     
    # define a variable to control the main loop
    running = True

    # main loop
    baba_test = BabaGraphic('you')
    water_test = WaterGraphic('you')
    wall_test = WallGraphic('you')
    skull_test = SkullGraphic('you') 

    while running:
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                print('bye')
                running = False
        
        baba_test.render(screen, 130, 150)
        water_test.render(screen, 230, 150)
        wall_test.render(screen, 330, 150)
        skull_test.render(screen, 430, 150)
        pygame.display.update()

