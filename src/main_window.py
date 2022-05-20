import sys
import os
current_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(current_dir, "."))

import pygame

from graphics import GameplayGraphics

class MainWindow():
    def __init__(self):
        pygame.init()
        # load and set the logo
        logo = pygame.image.load(os.path.join(current_dir, "../resources/graphics/baba.png"))
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Baba Is You")
        self.window_width = 1600
        self.window_height = 900

        self.screen = pygame.display.set_mode((self.window_width,self.window_height))
        self.background_music = pygame.mixer.music.load(os.path.join(current_dir, '../resources/graphics/Music.mp3'))
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.1)


    def open_main_menu(self):
        self.screen.fill(('black'))
        # draw banner and buttons
        self.scene = 'menu'
        main_banner = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banner_button/banner_main_menu.png"))

        self.screen.blit(main_banner,((self.screen.get_width()-main_banner.get_width())/2,(self.screen.get_height()-main_banner.get_height())/2))

        level_1_button = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banner_button/level_1.png"))
        level_1_button = pygame.transform.scale(level_1_button, (level_1_button.get_width()/2, level_1_button.get_height()/2))

        self.level_1_button_rect = level_1_button.get_rect(center=(self.screen.get_width()*0.25,self.screen.get_height()*0.75))
        self.screen.blit(level_1_button, self.level_1_button_rect)
        print(self.level_1_button_rect.topleft)

        level_2_button = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banner_button/level_2.png"))
        level_2_button = pygame.transform.scale(level_2_button, (level_2_button.get_width()/2, level_2_button.get_height()/2))

        self.level_2_button_rect = level_2_button.get_rect(center=(self.screen.get_width()*0.75,self.screen.get_height()*0.75))
        self.screen.blit(level_2_button, self.level_2_button_rect)
        print(self.level_2_button_rect.topleft)

        # get event
        self.running = True
        getting_level = True
        while getting_level and self.running:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    print(position)
                    self.level = self.get_level(position)
                    if self.level > 0:
                        self.scene = 'gameplay'
                        getting_level = False
                elif event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    print('bye')
                    self.running = False

            pygame.display.update()
        if self.scene == 'gameplay':
            self.open_gameplay(self.level)
        
    def get_level(self,position:pygame.mouse):
        if self.level_1_button_rect.collidepoint(position):
            return 1
        elif self.level_2_button_rect.collidepoint(position):
            return 2
        else:
            return -1

    def pop_up_win(self):
        win_banner = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banner_button/you_win.png"))

        self.screen.blit(win_banner,((self.screen.get_width()-win_banner.get_width())/2,(self.screen.get_height()-win_banner.get_height())/2))

        reset_button = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banner_button/reset_game.png"))
        reset_button = pygame.transform.scale(reset_button, (reset_button.get_width()/2, reset_button.get_height()/2))

        self.reset_button_rect = reset_button.get_rect(center=(self.screen.get_width()/2,self.screen.get_height()*0.75))
        self.screen.blit(reset_button, self.reset_button_rect)
        print(self.reset_button_rect.topleft)


    def pop_up_lose(self):
        lose_banner = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banner_button/you_lose.png"))

        self.screen.blit(lose_banner,((self.screen.get_width()-lose_banner.get_width())/2,(self.screen.get_height()-lose_banner.get_height())/2))

        reset_button = pygame.image.load(os.path.join(current_dir, "../resources/graphics/banner_button/reset_game.png"))
        reset_button = pygame.transform.scale(reset_button, (reset_button.get_width()/2, reset_button.get_height()/2))

        self.reset_button_rect = reset_button.get_rect(center=(self.screen.get_width()/2,self.screen.get_height()*0.75))
        self.screen.blit(reset_button, self.reset_button_rect)
        print(self.reset_button_rect.topleft)

    def open_gameplay(self, level):
        self.screen.fill(('black'))
        self.level = level
        self.scene = 'gameplay'

        self.gameplay = GameplayGraphics(0,0)

        if self.level == 1:
            self.gameplay.load_map(os.path.join(current_dir,'../resources/maps/map_1.csv'),os.path.join(current_dir,'../resources/maps/map_1.info'))
        
        elif self.level == 2:
            self.gameplay.load_map(os.path.join(current_dir,'../resources/maps/map_2.csv'),os.path.join(current_dir,'../resources/maps/map_2.info'))
        print(self.gameplay)
        
        self.running = True
        
        self.gameplay.get_rules()
        self.gameplay.apply_rules()
        self.gameplay.render(self.screen)
        
        pygame.display.update()
        self.run_gameplay()
        if self.scene == 'endgame':
            self.process_endgame_screen()


    def run_gameplay(self):
        while self.running and self.scene == 'gameplay':
            for event in pygame.event.get():
                self.process_event(event)

            pygame.display.update()
    
    def process_endgame_screen(self):
        self.scene = 'endgame'
        while self.running and self.scene == 'endgame':
            for event in pygame.event.get():
                self.process_event(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    position = pygame.mouse.get_pos()
                    if self.reset_button_rect.collidepoint(position):
                        self.scene = 'menu'
                    
                elif event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    print('bye')
                    self.running = False
            pygame.display.update()
        if self.scene == 'menu':     
            self.open_main_menu()

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
                self.scene = 'endgame'
            elif self.gameplay.check_lose():
                # self.running = False
                self.pop_up_lose()
                self.scene = 'endgame'
    
if __name__ == '__main__':
    main_window = MainWindow()
    main_window.open_main_menu()



            


