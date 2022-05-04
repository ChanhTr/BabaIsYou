# import the pygame module, so you can use it
import pygame
import os

current_dir = os.path.dirname(__file__)
 
# define a main function
def main():
     
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
    logo_resized = pygame.transform.scale(logo,(logo.get_width()/6,logo.get_height()/6))
    # main loop
    while running:
        
        screen.blit(logo_resized,((screen.get_width()-logo_resized.get_width())/2,(screen.get_height()-logo_resized.get_height())/2))
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                print('bye')
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print('move left')
                elif event.key == pygame.K_d:
                    print('move right')
                elif event.key == pygame.K_w:
                    print('move up')
                elif event.key == pygame.K_s:
                    print('move down')
                else:
                    print('not a move')
        pygame.display.update()
                
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()