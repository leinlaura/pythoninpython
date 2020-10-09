import pygame
import time
import random

#initialising pygame
pygame.init()

#colours for usage later
white = (255, 255, 255)
#yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
#....................


dis_width = 300
dis_height = 300
 
dis = pygame.display.set_mode((dis_width, dis_height)) #setting display height and width
pygame.display.set_caption('Snake Game by Laura') #name tag
 
clock = pygame.time.Clock()
 
snake_block = 10 #size of snake block
font_style = pygame.font.SysFont("Impact", 30) #font style for messages

 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, blue, [int(x[0]), int(x[1]), snake_block, snake_block])
 
 
def gameLoop():
    game_over = False
    game_close = False

    #startpoint of snake
    x1 = dis_width / 2  
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1 #length of snake blogs
    snake_speed = 5 #initial snake speed

    #random x and y coordinates for food appearance
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) *10.0 
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) *10.0  

    #main game loop
    while not game_over:
 
        while game_close == True: 
            dis.fill(black)
            messages = ["YOU LOST! SCORE: {sc}".format(sc= Length_of_snake),"PLAY AGAIN: PRESS C",
                        "      QUIT: PRESS Q"]
            n = 70
            for element in messages:
                msg = font_style.render(element, True, red)
                dis.blit(msg, [int(dis_width / 8), n])
                n = n + 50                        

           #mesg1 = font_style.render("YOU LOST! SCORE: {sc}".format(sc= Length_of_snake), True, red)
           # dis.blit(mesg1, [int(dis_width / 8), int(dis_height / 6)]) #position of message
         #   mesg2 = font_style.render("PLAY AGAIN: PRESS C".format(sc= Length_of_snake), True, red)
        #    dis.blit(mesg2, [int(dis_width / 8), int(dis_height / 3)])
            #mesg3 = font_style.render("QUIT: PRESS Q".format(sc= Length_of_snake), True, red)
          #  dis.blit(mesg3, [int(dis_width / 5), int(dis_height / 2)])#
            pygame.display.update()
    
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                #if Q is pressed the game is closed
                    if event.key == pygame.K_c:
                        gameLoop()
                    # if C is pressed the game starts again from the beginning
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True #game over if window is closed
            if event.type == pygame.KEYDOWN:
                #keypresses to change direction
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_q: #option to kill a game without failing
                        game_over = True
                        game_close = False
                    
        # if snake runs into an edge it reappears on the other side
        if x1 >= dis_width:
            x1 = 0
        if x1 < 0:
            x1 = dis_width
        if y1 >= dis_height:
            y1 = 0
        if y1 < 0:
            y1 = dis_height
        
            

        #position of snake head is changed    
        x1 += x1_change 
        y1 += y1_change
        dis.fill(black)
        #random food appears
        pygame.draw.rect(dis, green, [int(foodx), int(foody), snake_block, snake_block])
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
           del snake_List[0]

        # if snake runs into itself again, the game is over
        for x in snake_List[:-1]: #last element in the snake_List
            if x == snake_Head:
                game_close = True
 
        #snake is drawn
        our_snake(snake_block, snake_List)
 
 
        pygame.display.update()

        #if snake head goes over food, new random food appears and the snake gains length += 1
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            snake_speed += 1.5 #snake speed increased by 2 when gaining length
            

        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()
