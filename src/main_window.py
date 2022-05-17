import sys
sys.path.append("D:\Study\Python\Project\BabaIsYou\src")

import pygame
import os
current_dir = os.path.dirname(__file__)

from graphics import GameplayGraphics

class MainWindow():
    def __init__(self):
        pass
    
    def open_main_menu(self):
        pass

    def pop_up_win(self):
        win_banner = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banner_button/you_win.png"))

        self.screen.blit(win_banner,((self.screen.get_width()-win_banner.get_width())/2,(self.screen.get_height()-win_banner.get_height())/2))

        reset_banner = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banner_button/reset_game.png"))
        reset_resized = pygame.transform.scale(reset_banner,(200,100))

        self.screen.blit(reset_resized,((self.screen.get_width()-reset_resized.get_width())/2,(self.screen.get_height()-reset_resized.get_height())*0.75))


    def pop_up_lose(self):
        lose_banner = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banner_button/you_lose.png"))

        self.screen.blit(lose_banner,((self.screen.get_width()-lose_banner.get_width())/2,(self.screen.get_height()-lose_banner.get_height())/2))

        reset_banner = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banner_button/reset_game.png"))
        reset_resized = pygame.transform.scale(reset_banner,(200,100))

        self.screen.blit(reset_resized,((self.screen.get_width()-reset_resized.get_width())/2,(self.screen.get_height()-reset_resized.get_height())*0.75))

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
        print(self.gameplay)

        self.window_width = self.gameplay.n_cols * 40
        self.window_height = self.gameplay.n_rows * 40

        self.screen = pygame.display.set_mode((self.window_width,self.window_height))
        

        self.running = True
        
        self.gameplay.get_rules()
        self.gameplay.apply_rules()
        self.gameplay.render(self.screen)
        
        pygame.display.update()

    def run_game(self):
        while self.running:
            for event in pygame.event.get():
                self.process_event(event)

            pygame.display.update()
    
    def process_event(self, event: pygame.event):
        if event.type == pygame.QUIT:
            # change the value to False, to exit the main loop
            print('bye')
            self.running = False

        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_a:
                self.gameplay.move_left()                               
            elif event.key == pygame.K_d:
                self.gameplay.move_right()   
            elif event.key == pygame.K_w:
                self.gameplay.move_up()                
            elif event.key == pygame.K_s:
                self.gameplay.move_down()
                
            
            self.gameplay.get_rules()
            self.gameplay.apply_rules()
            self.screen.fill(('black'))
            self.gameplay.render(self.screen)

            if self.gameplay.check_win():
                # self.running = False
                self.pop_up_win()
            elif self.gameplay.check_lose():
                # self.running = False
                self.pop_up_lose()
    
if __name__ == '__main__':
    main_window = MainWindow()
    main_window.start_game(2)
    main_window.run_game()


            


