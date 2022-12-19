import pygame
import random
import os

pygame.mixer.init()
pygame.init()

# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
pink = (233, 210, 229)
dark_violet = (191, 99, 250)

screen_width = 900
screen_height = 500
gamewindow = pygame.display.set_mode((screen_width, screen_height))

bgimg = pygame.image.load("images.jpg")
bgimg = pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()

bgimg1 = pygame.image.load("snake.jpg")
bgimg1 = pygame.transform.scale(bgimg1,(screen_width,screen_height)).convert_alpha()

bgimg2 = pygame.image.load("img2.jpg")
bgimg2 = pygame.transform.scale(bgimg2,(screen_width,screen_height)).convert_alpha()

pygame.display.set_caption(("Snake Game with Umesh"))
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])


def plot_snake(gamewindow, color, snk_lst, snake_size):
    for x, y in snk_lst:
        pygame.draw.rect(gamewindow, black, [x, y, snake_size, snake_size])


def welcome():
    exit_game = False
    while not exit_game:
        gamewindow.fill(pink)
        gamewindow.blit(bgimg1,(0,0))
        text_screen("Welcome to Snake Game", black, 260, 180)
        text_screen("Press Space button to play game", black, 210, 220)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()

        pygame.display.update()
        clock.tick(40)


def game_loop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    snake_size = 10
    velocity_x = 0
    velocity_y = 0

    with open("highscore.txt", "r") as f:
        HighScore = f.read()

    snk_lst = []
    snk_length = 1

    fps = 50
    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(HighScore))

            gamewindow.fill(pink)
            # gamewindow.blit(bgimg2,(0,0))

            text_screen("GAME OVER!", red, 335, 115)
            text_screen("Please Enter to continue  ~~> ", red, 250, 170)
            text_screen("Score : "+ str(score), dark_violet, 250, 230)
            text_screen("Highscore : "+ str(HighScore), black, 250, 280)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()


        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 4
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -4
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -4
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = 4
                        velocity_x = 0
                    if event.key == pygame.K_q:
                        score += 10

                    if abs(snake_x - food_x) < 10 and abs(snake_y - snake_y) < 10:
                        score += 10
                        food_x = random.randint(20, screen_width / 2)
                        food_y = random.randint(20, screen_height / 2)
                        snk_length += 4

                        if score > int(HighScore):
                            HighScore = score

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            gamewindow.fill(white)
            gamewindow.blit(bgimg,(0,0))
            text_screen("Score : " + str(
                score) + "                                                                   Highscore : " + str(
                HighScore), red, 1, 1)
            pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_lst.append(head)

            if len(snk_lst) > snk_length:
                del snk_lst[0]

            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
            if head in snk_lst[:-1]:
                game_over = True

            plot_snake(gamewindow, black, snk_lst, snake_size)

        pygame.display.update()

        clock.tick(fps)

    pygame.quit()
    quit()


welcome()
