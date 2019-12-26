import pygame
import random
import math

pygame.init()

# colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
ORANGE = (255, 200, 0)
PINK = (255, 100, 100)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DarkBlue = (0, 0, 128)

# window
window_size = (500, 300)
window = pygame.display.set_mode(window_size)
window.fill(BLACK)
pygame.display.set_caption('Pong Game')
pygame.display.update()

# positions
circlePos = [window_size[0]//2, window_size[1]//2]
circleRad = 5
rectPos1 = [10, window_size[1]//2, 5, 50]
rectPos2 = [window_size[0] - 15, window_size[1]//2, 5, 50]
rectPos_player1 = [150, 30, 30, 20]
rectPos_player2 = [window_size[0] - 180, 30, 30, 20]

Scores = [0, 0]

#Text

font = pygame.font.SysFont("Ubuntu", 10)
player1 = font.render("Player 1", True, WHITE)
player2 = font.render("Player 2", True, WHITE)
player1_Score = font.render(str(Scores[0]), True, WHITE)
player2_Score = font.render(str(Scores[1]), True, WHITE)


# velocity
vel_rect1 = [0, 0]
vel_rect2 = [0, 4]
vel_circle = [random.choice([-6, -5, 5, 6]), random.choice([-6, -5, 0, 5, 6])]


#FUNCTIONS

STATE = False
isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                vel_rect1[1] = -4
            elif event.key == pygame.K_DOWN:
                vel_rect1[1] = +4

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                vel_rect1[1] = 0
            elif event.key == pygame.K_DOWN:
                vel_rect1[1] = 0

    if max(Scores) == 10:
        STATE = True
        isRunning = False

    
    pygame.time.wait(20)

    circlePos[0] += vel_circle[0]
    circlePos[1] += vel_circle[1]

    if (0 >= rectPos1[1] + vel_rect1[1] ):
        vel_rect1[1] = 0
    else:
        rectPos1[1] += vel_rect1[1]
    
    if (rectPos1[1] + vel_rect1[1] >= window_size[1] - (rectPos1[3])):
        vel_rect1[1] = 0
    else:
        rectPos1[1] += vel_rect1[1]


    add_dist = abs((rectPos2[1] + rectPos2[3]//2 + vel_rect2[1]) - (circlePos[1] + vel_circle[1])) 
                #(rectPos2[0] + rectPos2[2]//2) - (circlePos[0] + vel_circle[0])**2)**(0.5))

    sub_dist = abs((rectPos2[1] + rectPos2[3]//2 - vel_rect2[1]) - (circlePos[1] + vel_circle[1])) 
                #(rectPos2[0] + rectPos2[2]//2) - (circlePos[0] + vel_circle[0])**2))
    if (-rectPos2[3]//2 <= rectPos2[1] <= window_size[1] + rectPos2[3]//2):
        if add_dist >= sub_dist:
            rectPos2[1] -= vel_rect2[1]
        else:
            rectPos2[1] += vel_rect2[1]
    else:
        vel_rect2[1] *= -1

    if not (circleRad <= circlePos[1] <= window_size[1] - circleRad):
        vel_circle[1] *= -1

    if (rectPos1[0] <= circlePos[0] <= rectPos1[0] + rectPos1[2]):
        if (rectPos1[1] <= circlePos[1] <= rectPos1[1] + rectPos1[3]):
            if vel_circle[0] < 0:
                vel_circle[0] *= -1
            else:
                vel_circle[1] *= -1

    if (rectPos2[0] + rectPos2[2] >= circlePos[0] >= rectPos2[0]):
        if (rectPos2[1] <= circlePos[1] <= rectPos2[1] + rectPos2[3]):
            if vel_circle[0] > 0:
                vel_circle[0] *= -1
            else:
                vel_circle[1] *= -1

    #starting over

    if circlePos[0] <= -circleRad:
        Scores[1] += 1
        circlePos = [window_size[0]//2, window_size[1]//2]
        rectPos1 = [10, window_size[1]//2, 5, 50]
        rectPos2 = [window_size[0] - 15, window_size[1]//2, 5, 50]
        window.fill(BLACK)
        window.blit(player1, (60, 10))
        window.blit(player2, (window_size[0] - 100, 10))
        player1_Score = font.render(str(Scores[0]), True, WHITE)
        player2_Score = font.render(str(Scores[1]), True, WHITE)
        window.blit(player1_Score, (60 + player1.get_width()//2, 30))
        window.blit(player2_Score, (window_size[0] - 100 + player2.get_width()//2, 30))
        pygame.draw.rect(window, WHITE, rectPos1)
        pygame.draw.rect(window, WHITE, rectPos2)
        pygame.draw.circle(window, WHITE, circlePos, circleRad)
        pygame.display.update()
        pygame.time.wait(500)
        vel_circle = [random.choice([-4, -3, 3, 4]), random.choice([-4, -3, 3, 4])]

    if circlePos[0] >= window_size[0] + circleRad:
        Scores[0] += 1
        circlePos = [window_size[0]//2, window_size[1]//2]
        rectPos1 = [10, window_size[1]//2, 5, 50]
        rectPos2 = [window_size[0] - 15, window_size[1]//2, 5, 50]
        window.fill(BLACK)
        window.blit(player1, (60, 10))
        window.blit(player2, (window_size[0] - 100, 10))
        player1_Score = font.render(str(Scores[0]), True, WHITE)
        player2_Score = font.render(str(Scores[1]), True, WHITE)
        window.blit(player1_Score, (60 + player1.get_width()//2, 30))
        window.blit(player2_Score, (window_size[0] - 100 + player2.get_width()//2, 30))
        pygame.draw.rect(window, WHITE, rectPos1)
        pygame.draw.rect(window, WHITE, rectPos2)
        pygame.draw.circle(window, WHITE, circlePos, circleRad)
        pygame.display.update()

        pygame.time.wait(500)
        vel_circle = [random.choice([-4, -3, 3, 4]), random.choice([-4, -3, 3, 4])]
    
    if not STATE:
        window.fill(BLACK)
        window.blit(player1, (60, 10))
        window.blit(player2, (window_size[0] - 100, 10))
        window.blit(player1_Score, (60 + player1.get_width()//2, 30))
        window.blit(player2_Score, (window_size[0] - 100 + player2.get_width()//2, 30))
        pygame.draw.circle(window, WHITE, circlePos, circleRad)
        pygame.draw.rect(window, WHITE, rectPos1)
        pygame.draw.rect(window, WHITE, rectPos2)
        pygame.display.update()

font = pygame.font.SysFont("Ubuntu", 50)

if STATE:
    isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
    window.fill(BLACK)
    pygame.display.update()
    pygame.time.wait(300)
    if Scores[0] == 10:
        last_Score = font.render("Player1 Won!", True, RED)
        window.blit(last_Score, (window_size[0]//2 - last_Score.get_width()//2, window_size[1]//2 - last_Score.get_height()//2))
    elif Scores[1] == 10:
        last_Score = font.render("Player2 Won!", True, RED)
        window.blit(last_Score, (window_size[0]//2 - last_Score.get_width()//2, window_size[1]//2 - last_Score.get_height()//2))
    # pygame.draw.lines(window, BLACK, False,
    #                 [(window_size[0]//2, 0), (window_size[0]//2, window_size[1])], 1)
    # pygame.draw.lines(window, BLACK, False,
    #                 [(0, window_size[1]//2), (window_size[0], window_size[1]//2)], 1)
    pygame.display.update()
    pygame.time.wait(300)
