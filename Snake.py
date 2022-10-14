import pygame
import random
 
pygame.init()

#Colors
purple = (179, 179, 255)
blue = (51, 204, 255)
black = (0, 0, 0)
red = (213, 50, 80)
 
display_width = 1280
display_height = 720
 
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')
 
clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 20
 
font_style = pygame.font.SysFont("hpsimplified", 30)
score_font = pygame.font.SysFont("hpsimplified", 17)
 
def gamescore(score):
    value = score_font.render("Score: " + str(score), True, purple)
    display.blit(value, [0, 0])
 
def snakeconstructor(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, blue, [x[0], x[1], snake_block, snake_block])
 
def message(msg):
    mesg = font_style.render(msg, True, purple)
    display.blit(mesg, [display_width / 3, display_height / 2.2])
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = display_width / 2
    y1 = display_height / 2
 
    x1_change = 0
    y1_change = 0
    prev="";
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    while not game_over:
 
        while game_close == True:
            display.fill(black)
            message("You Lost! Press: P: Play Again  Q: Quit")
            gamescore(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT and prev !="right"):
                    x1_change = -snake_block
                    y1_change = 0
                elif (event.key == pygame.K_RIGHT and prev !="left"):
                    x1_change = snake_block
                    y1_change = 0
                elif (event.key == pygame.K_UP and prev !="down"):
                    x1_change = 0
                    y1_change = -snake_block
                elif (event.key == pygame.K_DOWN and prev !="up"):
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True

        if x1<x1+x1_change:
            prev="right"
        elif x1>x1+x1_change:
            prev="left"
        elif y1<y1+y1_change:
            prev="down"
        elif y1>y1+y1_change:
            prev="up"

        x1 += x1_change
        y1 += y1_change
        display.fill(black)
        pygame.draw.rect(display, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        snakeconstructor(snake_block, snake_List)
        gamescore(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
gameLoop()