
import random
import sys
import time
import pygame
from pygame.locals import *
pygame.init()


fps = 60
screen_width = 900
screen_height = 600
gamewindow = pygame.display.set_mode((screen_width,screen_height),pygame.SRCALPHA)

game_images ={}
game_sound ={}
bird ='gallery/images/bird.png'
pillar ='gallery/images/pillar.png'
background ='gallery/images/background.jpeg'
base = 'gallery/images/base.jpeg'
 
white =(255,255,255)
red =(255,0,0)
green =(0,255,0)
blue = (0,0,255)
black = (0,0,0)

font = pygame.font.SysFont(None,40)
red =(255,0,0)
exit_game =False
game_over = False
base_y = int(screen_width/2)

#pillar properties
pillar_x = random.randint(800,900)
pillar_y = random.randint(-300,-100)
pillar_gap = 200
pillar_speed =10

def gameloop():
    exit_game = False
    game_over = False
    bird_x = 100
    bird_y = 50
    score = 0
    pillar_x = random.randint(400,600)
    pillar_y = random.randint(-300,-100)

 
    



    while not exit_game:
        if game_over:
            gameov()
           

        
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_ESCAPE:
                        welcome_screen()
                    if event.key == pygame.K_UP or pygame.K_SPACE:
                       if bird_y > 0:
                        bird_y-=45


            
            bird_y+=2
            pillar_x -= 4
            if bird_y >= base_y-30 or bird_y <= 0:
                game_over = True
            if game_over == True:
                gamewindow.blit(game_images['background'],(0,0))
            if bird_y >= base_y:
                game_over =True
            if pillar_x <= -80:
                pillar_x = 950
                pillar_y = random.randint(-300,-100)
                score += 1
                #print(score)
                
            if bird_y <= pillar_y+425 and (bird_x <= pillar_x+30 and bird_x >= pillar_x):
                game_over = True
                time.sleep(1)
            if bird_y >= pillar_y+580 and (bird_x <= pillar_x+30 and bird_x >= pillar_x):
                game_over = True
                time.sleep(1)

             
 


            gamewindow.blit(game_images['background'],(0,0))
            text_screen("score: "+ str(score),black,721,23)
            gamewindow.blit(game_images['pillar'][0],( pillar_x,pillar_y))
            gamewindow.blit(game_images['pillar'][1],(pillar_x,pillar_y+580))
            #text_screen("score: "+ str(score),black,721,23)
            
            #pygame.draw.rect(gamewindow,red,(pillar_x+90,pillar_y+425,10,10)) helps to find pillar image cords



                  
            gamewindow.blit(game_images['bird'],(bird_x,bird_y)) 
            gamewindow.blit(game_images['base'],(0,base_y))
            pygame.display.update()     
            fpsclock.tick(fps)

def welcome_screen():
    bird_x = 100
    bird_y = 50
    


    
    message_x = int(screen_width/2)
    message_y = int(screen_height/2)
    exit_game = False
    while not exit_game:
        
        gamewindow.fill((255,255,255))
        gamewindow.blit(game_images['background'],(0,0))
        gamewindow.blit(game_images['bird'],(bird_x,bird_y))
        gamewindow.blit(game_images['base'],(0,base_y))
        #gamewindow.blit(game_images['pillar'][0],(0,0))
        #pygame.draw.rect(gamewindow,red,(bird_x+50,bird_y+40,10,10))
        #pygame.draw.rect(gamewindow,red,(90,425,10,10))
        text_screen("Press Enter TO Play !",red,290,480)
        pygame.display.update()
        fpsclock.tick(fps)
        
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT :
                exit_game = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    gameloop() 
                if event.key == pygame.K_ESCAPE:
                    exit_game = True
    pygame.quit()
    sys.exit()

def gameov():
     gamewindow.fill(white)
     text_screen("press enter to play",red,300,300)
     pygame.display.update()
     for event in pygame.event.get():
         if event.type == QUIT:
             pygame.quit()
             sys.exit()

         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_RETURN:
                 
                 gameloop()
             if event.key == pygame.K_ESCAPE:
                 welcome_screen()
        

def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gamewindow.blit(screen_text,[x,y])


                       
                
if __name__ == "__main__":
    pygame.init()
    fpsclock = pygame.time.Clock()
    pygame.mixer.init()
    pygame.display.set_caption("Floppy Bird")
    
    #game images
    #game_images['numbers']
    #game_images['base'] = pygame.image.load(base).convert_alpha()
    game_images['pillar'] = (
       pygame.transform.rotate(pygame.image.load(pillar).convert_alpha(),180),
       pygame.image.load(pillar).convert_alpha()
         )
    game_images['background'] = pygame.image.load(background).convert_alpha()
    game_images['bird'] = pygame.image.load(bird).convert_alpha()
    game_images['base'] = pygame.image.load(base).convert_alpha()
    
    #game sound
    game_sound['bird_fall'] = pygame.mixer.Sound('gallery/audio/bird_fall.wav')
    game_sound['blip'] = pygame.mixer.Sound('gallery/audio/blip.wav')
    game_sound['game_end'] = pygame.mixer.Sound('gallery/audio/game_end.wav')
    game_sound['game_opener'] = pygame.mixer.Sound('gallery/audio/game_opener.wav')
    game_sound['score_up'] = pygame.mixer.Sound('gallery/audio/score_up.wav')

 
    welcome_screen()
    gameloop()

 











