import pygame
import random

pygame.init()
game_width = 1000
game_height = 650
screen = pygame.display.set_mode((game_width, game_height))
clock = pygame.time.Clock()
running = True
true = False
level = 1
reset_player = False
wall_collsion = False


# adding pictures
background_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/platform.png")
player_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/red.png" )
exit_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/exit.png")
player_pic = pygame.transform.scale(player_pic, (50, 50))
exit_pic = pygame.transform.scale(exit_pic, (60,60))
spike1_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/spike1.png")
spike1_pic = pygame.transform.scale(spike1_pic, (50,50))
coin_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/coin1.png")
coin_pic = pygame.transform.scale(coin_pic, (40,40))
# blit var's
scroll_x = 0
scroll_y = 0
player_x = 100
player_y = 385
exit_x = 900
exit_y = 300
spike1_x = 750
spike1_y = 275
spike2_x = 400
spike2_y = 385
lava_x = 300
lava_y = 400
lava2_x = 200
lava2_y = 400
wall_x = 600
wall_y = 400

def update(pic, screen,x,y):
    screen.blit(pic, (x,y))

    


                
            
                




while running:
    # Makes the game stop if the player clicks the X or presses esc
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
               running = False
    update(background_pic,screen,scroll_x,scroll_y)
    update(player_pic,screen,player_x,player_y)
    update(exit_pic,screen,exit_x,exit_y)
    
    

   
    
        
        

    
    # adding movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_y += -5
    if keys[pygame.K_RIGHT]:
        player_x += +5
    if keys[pygame.K_LEFT]:
        player_x += -5
    if not keys[pygame.K_UP]:
        player_y += +5
        if player_y == 385:
            player_y += 1
        else:
            player_y = 385
        
        
    

    # adding one to the level and exiting.
    if player_x == exit_x and player_y == exit_y or player_x == 875 and player_y == 275:
            level += 1
            reset_player = True
                


      
    if level == 2:
            wall_collsion = False
            true = True
            spike1_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/spike1.png")
            spike1_pic = pygame.transform.scale(spike1_pic, (50,50))

            spike2_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/spike2.png")
            spike2_pic = pygame.transform.scale(spike2_pic, (50,50))
            
            update(spike1_pic,screen,spike1_x,spike1_y)
            update(spike2_pic,screen,spike2_x,spike2_y)
            if reset_player:
                player_x = 100
                player_y = 385
                reset_player = False
                true = True
                
            if player_x == 735 or player_x == 725 or player_x == 700 or player_x == spike1_x:
                if player_y == 250 or player_y == 275 or player_y == 260:
                    if true == True:
                        true = False
                        print("Your died.")
                        print( f'{level} thats the level you finised in.')
                        exit()
                    
            if player_x == 390 or player_x == 385:
                if player_y == 385:
                    if true == True:
                        print("Your died")
                        print( f'{level} thats the level you finished in.')
                        exit()
    elif level == 3:
             wall_collsion = False
             lava1_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/lava.png")
             lava1_pic = pygame.transform.scale(lava1_pic, (50,50))
             lava2_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/lava2.png")
             lava2_pic = pygame.transform.scale(lava2_pic, (50,50))
             
             update(lava1_pic,screen,lava_x,lava_y)
             update(lava2_pic,screen,lava2_x,lava2_y)
             if reset_player:
                true == True
                player_x = 100
                player_y = 385
                reset_player = False
             if player_x == 295 or player_x == lava_x or player_x == 290:
                if player_y == 395 or player_y == lava_y or player_y == 385:
                        if true == True:
                            print("you died")
                            print(f'{level} thats the level you finished in.')
                            exit()
             if player_y == 395 or player_y == lava2_y or player_y == 385:
                if player_x == 195  or player_x == 190 or player_x == lava2_x:
                    if true == True:
                        print("you died")
                        print(f'{level} thats the level you finished in.')
                        exit()
        
        
    elif level == 4:
            wall_collsion = False
            true = True
            wall_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/wall2.png")
            wall_pic = pygame.transform.scale(wall_pic, (50,50))
            spike1_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/spike1.png")
            spike1_pic = pygame.transform.scale(spike1_pic, (50,50))
            spike2_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/spike2.png")
            spike2_pic = pygame.transform.scale(spike2_pic, (50,50))
            
            update(wall_pic,screen,wall_x,wall_y)
            update(spike1_pic,screen,spike1_x,spike1_y)
            update(spike2_pic,screen,spike2_x,spike2_y)
            if reset_player:
                player_x = 100
                player_y = 385
                reset_player = False
                true = True
                wall_collsion = True
                    
            if player_x == 725 or player_x == 735 or  player_x == 720 or player_x == spike1_x :
                if player_y == 250 or player_y == 275 or player_x == 265:
                    if true == True:
                        true = False
                        print("Your died.")
                        print( f'{level} thats the level you finised in.')
                        exit()
                        
            if player_x == 390 or player_x == 385:
                if player_y == 385:
                    if true == True:
                        print("Your died")
                        print( f'{level} thats the level you finished in.')
                        exit()

            if player_x ==575 or player_x == 585 or player_x == 595 or player_x == 600:
                if player_y == 385 or player_y == 395 or player_y == 400:
                    if true == True:
                        print("Your died.")
                        print(f'{level} thats the level you finshed in.')
                        exit()
    elif level == 5:
            true = True
            wall_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/wall2.png")
            wall_pic = pygame.transform.scale(wall_pic, (50,50))
            spike1_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/spike1.png")
            spike1_pic = pygame.transform.scale(spike1_pic, (50,50))
            spike2_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/spike2.png")
            spike2_pic = pygame.transform.scale(spike2_pic, (50,50))
            lava1_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/lava.png")
            lava1_pic = pygame.transform.scale(lava1_pic, (50,50))
            lava2_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/lava2.png")
            lava2_pic = pygame.transform.scale(lava2_pic, (50,50))
            
            update(wall_pic,screen,wall_x,wall_y)
            update(spike1_pic,screen,spike1_x,spike1_y)
            update(spike2_pic,screen,spike2_x,spike2_y)
            update(lava1_pic,screen,lava_x,lava_y)
            update(lava2_pic,screen,lava2_x,lava2_y)
            if reset_player:
                player_x = 100
                player_y = 385
                reset_player = False
                true = True
                wall_collsion = True
                    
            if player_x == 725 or player_x == 720 or player_x == 735 or player_x == spike1_x:
                if player_y == 250 or player_y == 275 or player_y == 265:
                    if true == True:
                        true = False
                        print("Your died.")
                        print( f'{level} thats the level you finised in.')
                        exit()
                        
            if player_x == 390 or player_x == 385:
                if player_y == 385:
                    if true == True:
                        print("Your died")
                        print( f'{level} thats the level you finished in.')
                        exit()

            if player_x ==575 or player_x == 585 or player_x == 595 or player_x == 600 or player_x == wall_x:
                if player_y == 385 or player_y == 395 or player_y == 400 or player_y == wall_y:
                    if true == True:
                        print("Your died.")
                        print(f'{level} thats the level you finshed in.')
                        exit()
            if player_x == 295 or player_x == lava_x or player_x == 290:
                if player_y == 395 or player_y == lava_y or player_y == 385:
                    if true == True:
                        print("you died")
                        print(f'{level} thats the level you finished in.')
                        exit()
            if player_y == 395 or player_y == lava2_y or player_y == 385:
                if player_x == 195  or player_x == 190 or player_x == lava2_x:
                    if true == True:
                        print("you died")
                        print(f'{level} thats the level you finished in.')
                        exit()
    elif level == 6:
            true = True
            wall_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/wall2.png")
            wall_pic = pygame.transform.scale(wall_pic, (50,50))
            lava1_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/lava.png")
            lava1_pic = pygame.transform.scale(lava1_pic, (50,50))
            lava2_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/lava2.png")
            lava2_pic = pygame.transform.scale(lava2_pic, (50,50))
            
            update(lava1_pic,screen,lava_x,lava_y)
            update(lava2_pic,screen,lava2_x,lava2_y)
            update(wall_pic,screen,wall_x,wall_y)
            wall_x = 400
            wall_y = 399
            if reset_player:
                player_x = 100
                player_y = 385
                reset_player = False
                true = True
                wall_collsion = True
            if player_x ==375 or player_x == 385 or player_x == 395 or player_x == 300 or player_x == wall_x:
                if player_y == 385 or player_y == 395 or player_y == 400 or player_y == wall_y:
                    if true == True:
                        print("Your died.")
                        print(f'{level} thats the level you finshed in.')
                        exit()
            if player_x == 295 or player_x == lava_x or player_x == 290:
                if player_y == 395 or player_y == lava_y or player_y == 385:
                    if true == True:
                        print("you died")
                        print(f'{level} thats the level you finished in.')
                        exit()
            if player_y == 395 or player_y == lava2_y or player_y == 385:
                if player_x == 195  or player_x == 190 or player_x == lava2_x:
                    if true == True:
                        print("you died")
                        print(f'{level} thats the level you finished in.')
                        exit()       
    elif level == 7:
            true = True
            lava1_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/lava.png")
            lava1_pic = pygame.transform.scale(lava1_pic, (50,50))
            lava2_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/lava2.png")
            lava2_pic = pygame.transform.scale(lava2_pic, (50,50))
            spike1_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/spike1.png")
            spike1_pic = pygame.transform.scale(spike1_pic, (50,50))
            spike2_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/spike2.png")
            spike2_pic = pygame.transform.scale(spike2_pic, (50,50))
            
            update(lava1_pic,screen,lava_x,lava_y)
            update(lava2_pic,screen,lava2_x,lava2_y)
            update(spike1_pic,screen,spike1_x,spike1_y)
            update(spike2_pic,screen,spike2_x,spike2_y)
            lava_x = 600
            lava_y = 310
            spike1_x = 700
            spike1_y = 375
            if reset_player:
                player_x = 100
                player_y = 385
                reset_player = False
                true = True
            if player_x == 595 or player_x == lava_x or player_x == 590:
                if player_y == 295 or player_y == lava_y or player_y == 285:
                    if true == True:
                        print("you died")
                        print(f'{level} thats the level you finished in.')
                        exit()   # second spike
            if player_x == 685 or player_x == 690 or player_x == 695 or player_x == spike1_x:
                if player_y == 350 or player_y == 375 or player_y == 365 or player_y == 385:
                    if true == True:
                        true = False
                        print("Your died.")
                        print( f'{level} thats the level you finised in.')
                        exit()
                # first spike               
                if player_x == 390 or player_x == 385 or player_x == 400:
                    if player_y == 385:
                        if true == True:
                            true = False
                            print("Your died")
                            print( f'{level} thats the level you finished in.')
                            exit()
                if player_y == 395 or player_y == lava2_y or player_y == 385:
                        if player_x == 195  or player_x == 190 or player_x == lava2_x:
                            if true == True:
                                print("you died")
                                print(f'{level} thats the level you finished in.')
                                exit()
    elif level == 8:
            true = True
            lava1_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/lava.png")
            lava1_pic = pygame.transform.scale(lava1_pic, (50,50))
            spike1_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/spike1.png")
            spike1_pic = pygame.transform.scale(spike1_pic, (50,50))
            spike2_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/spike2.png")
            spike2_pic = pygame.transform.scale(spike2_pic, (50,50))
            
            update(lava1_pic,screen,lava_x,lava_y)
            update(spike1_pic,screen,spike1_x,spike1_y)
            update(spike2_pic,screen,spike2_x,spike2_y)
            lava_x = 600
            lava_y = 310
            spike1_x = 700
            spike1_y = 375
            if reset_player:
                player_x = 100
                player_y = 385
                reset_player = False
                true = True
                
            if player_x == 685 or player_x == 690 or player_x == 695 or player_x == spike1_x:
                if player_y == 350 or player_y == 375 or player_y == 365 or player_y == 385:
                    if true == True:
                        true = False
                        print("Your died.")
                        print( f'{level} thats the level you finised in.')
                        exit()
            if player_x == 595 or player_x == lava_x or player_x == 590:
                if player_y == 295 or player_y == lava_y or player_y == 285:
                    if true == True:
                        print("you died")
                        print(f'{level} thats the level you finished in.')
                        exit()
            if player_x == 390 or player_x == 385:
                if player_y == 385:
                    if true == True:
                        true = False
                        print("Your died")
                        print( f'{level} thats the level you finished in.')
                        exit()
    elif level == 9:
            true = True
            wall_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/wall2.png")
            wall_pic = pygame.transform.scale(wall_pic, (50,50))
            spike2_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/spike2.png")
            spike2_pic = pygame.transform.scale(spike1_pic, (50,50))
            
            update(wall_pic,screen,wall_x,wall_y)
            update(spike2_pic,screen,spike2_x,spike2_y)
            wall_x = 400
            wall_y = 399
            spike2_x = 700
            spike2_y = 375
            if reset_player:
                player_x = 100
                player_y = 385
                reset_player = False
                true = True
            if player_x == 685 or player_x == 690 or player_x == 695 or player_x == spike2_x:
                if player_y == 350 or player_y == 375 or player_y == 365 or player_y == 385:
                    if true == True:
                       true = False
                       print("Your died.")
                       print( f'{level} thats the level you finised in.')
                       exit()
            if player_x ==375 or player_x == 385 or player_x == 395 or player_x == wall_x:
                if player_y == 385 or player_y == 395 or player_y == 400 or player_y == wall_y:
                    if true == True:
                        print("Your died.")
                        print(f'{level} thats the level you finshed in.')
                        exit()
    elif level == 10:
            true = True
            lava1_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/lava.png")
            lava1_pic = pygame.transform.scale(lava1_pic, (50,50))
            wall_pic = pygame.image.load("/Users/zachthelen/Desktop/untitled folder/assets/wall2.png")
            wall_pic = pygame.transform.scale(wall_pic, (50,50))
            
            update(wall_pic,screen,wall_x,wall_y)
            update(lava1_pic,screen,lava_x,lava_y)
            update(lava2_pic,screen,lava2_x,lava2_y)
            wall_x = 400
            wall_y = 399
            lava_x = 600
            lava_y = 310
            if reset_player:
                player_x = 100
                player_y = 385
                reset_player = False
                true = True
            if player_x ==375 or player_x == 385 or player_x == 395 or player_x == wall_x:
                if player_y == 385 or player_y == 395 or player_y == 400 or player_y == wall_y:
                    if true == True:
                        print("Your died.")
                        print(f'{level} thats the level you finshed in.')
                        exit()
            if player_x == 595 or player_x == lava_x or player_x == 590:
                if player_y == 295 or player_y == lava_y or player_y == 285:
                    if true == True:
                        print("you died")
                        print(f'{level} thats the level you finished in.')
                        exit()
               
            if player_y == 395 or player_y == lava2_y or player_y == 385:
                if player_x == 195  or player_x == 190 or player_x == lava2_x:
                    if true == True:
                        print("you died")
                        print(f'{level} thats the level you finished in.')
                        exit()
        
    # tell screen to update
    pygame.display.flip()
    clock.tick(50)
    pygame.display.set_caption(" square jump fps: " + str(clock.get_fps()))
