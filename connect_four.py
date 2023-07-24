from random import*
import pygame
from time import*
from playsound import playsound
import threading

pygame.init()

surface = pygame.display.set_mode((350,300))
event = pygame.event.get()


x = 0
y = 0

fallen_blocks = []

player1_name = "PLAYER 1"
player2_name = "PLAYER 2"
turn = "Player 1"

fall_switch = 0

player1_color = (0,0,255)
player2_color = (255,0,0)
#player1_color = (randint(10,240),randint(10,240),randint(10,240))
#player2_color = (randint(10,240),randint(10,240),randint(10,240))

win_state = False



def win():
    global win_state
    pygame.image.save(surface,"win_screenshot.png")
    win_state = True

    quit()

def grid_update():
    grid_y = -50

    for i in range(14):
        grid_y = grid_y+50
        grid_x = -50
        for j in range(20):
            grid_x = grid_x+50
            pygame.draw.rect(surface, (255,255,255), pygame.Rect(grid_x, grid_y, 50, 50),1)

def win_checker():
    global turn


    for i in range(len(fallen_blocks)):
        if fallen_blocks[i][2] != turn:
            temp_x = fallen_blocks[i][0]
            temp_y = fallen_blocks[i][1]



            for j in range(len(fallen_blocks)):
                if fallen_blocks[j][0] == temp_x and fallen_blocks[j][2] != turn and fallen_blocks[j][1] == temp_y:
                    temp_x = temp_x+50

                    for j in range(len(fallen_blocks)):
                        if fallen_blocks[j][0] == temp_x and fallen_blocks[j][2] != turn and fallen_blocks[j][1] == temp_y:
                            temp_x = temp_x+50

                            for j in range(len(fallen_blocks)):
                                if fallen_blocks[j][0] == temp_x and fallen_blocks[j][2] != turn and fallen_blocks[j][1] == temp_y:
                                    temp_x = temp_x+50

                                    for j in range(len(fallen_blocks)):
                                        if fallen_blocks[j][0] == temp_x and fallen_blocks[j][2] != turn and fallen_blocks[j][1] == temp_y:
                                            temp_x = temp_x+50
                                            win()

            temp_x = fallen_blocks[i][0]

            for j in range(len(fallen_blocks)):
                if fallen_blocks[j][0] == temp_x and fallen_blocks[j][2] != turn and fallen_blocks[j][1] == temp_y:
                    temp_y = temp_y+50

                    for j in range(len(fallen_blocks)):
                        if fallen_blocks[j][0] == temp_x and fallen_blocks[j][2] != turn and fallen_blocks[j][1] == temp_y:
                            temp_y = temp_y+50

                            for j in range(len(fallen_blocks)):
                                if fallen_blocks[j][0] == temp_x and fallen_blocks[j][2] != turn and fallen_blocks[j][1] == temp_y:
                                    temp_y = temp_y+50

                                    for j in range(len(fallen_blocks)):
                                        if fallen_blocks[j][0] == temp_x and fallen_blocks[j][2] != turn and fallen_blocks[j][1] == temp_y:
                                            temp_y = temp_y+50
                                            win()


            temp_y = fallen_blocks[i][1]

            for j in range(len(fallen_blocks)):
                if fallen_blocks[j][0] == temp_x and fallen_blocks[j][2] != turn and fallen_blocks[j][1] == temp_y:
                    temp_y = temp_y-50
                    temp_x = temp_x+50

                    for j in range(len(fallen_blocks)):
                        if fallen_blocks[j][0] == temp_x and fallen_blocks[j][2] != turn and fallen_blocks[j][1] == temp_y:
                            temp_y = temp_y-50
                            temp_x = temp_x+50

                            for j in range(len(fallen_blocks)):
                                if fallen_blocks[j][0] == temp_x and fallen_blocks[j][2] != turn and fallen_blocks[j][1] == temp_y:
                                    temp_y = temp_y-50
                                    temp_x = temp_x+50

                                    for j in range(len(fallen_blocks)):
                                        if fallen_blocks[j][0] == temp_x and fallen_blocks[j][2] != turn and fallen_blocks[j][1] == temp_y:
                                            temp_y = temp_y-50
                                            temp_x = temp_x+50
                                            win()


            temp_x = fallen_blocks[i][0]
            temp_y = fallen_blocks[i][1]

            for j in range(len(fallen_blocks)):
                if fallen_blocks[j][0] == temp_x and fallen_blocks[j][2] != turn and fallen_blocks[j][1] == temp_y:
                    temp_y = temp_y+50
                    temp_x = temp_x+50

                    for j in range(len(fallen_blocks)):
                        if fallen_blocks[j][0] == temp_x and fallen_blocks[j][2] != turn and fallen_blocks[j][1] == temp_y:
                            temp_y = temp_y+50
                            temp_x = temp_x+50

                            for j in range(len(fallen_blocks)):
                                if fallen_blocks[j][0] == temp_x and fallen_blocks[j][2] != turn and fallen_blocks[j][1] == temp_y:
                                    temp_y = temp_y+50
                                    temp_x = temp_x+50

                                    for j in range(len(fallen_blocks)):
                                        if fallen_blocks[j][0] == temp_x and fallen_blocks[j][2] != turn and fallen_blocks[j][1] == temp_y:
                                            temp_y = temp_y+50
                                            temp_x = temp_x+50
                                            win()


        
            

def fall():
    global y
    global fall_switch
    global turn
    global fallen_blocks

    y = y+50

    for i in range(len(fallen_blocks)):
        if x == fallen_blocks[i][0] and y == fallen_blocks[i][1]:
            fall_switch = 0

            fallen_blocks.append((x,y-50,turn))

            y = 0

            if turn == "Player 1":
                turn = "Player 2"
            else:
                turn = "Player 1"


    if y == 250:
        fall_switch = 0

        fallen_blocks.append((x,y,turn))

        y = 0

        if turn == "Player 1":
            turn = "Player 2"
        else:
            turn = "Player 1" 


def draw():
    if turn == "Player 1":
        pygame.draw.rect(surface, player1_color, pygame.Rect(x, y, 45, 45))
    else:
        pygame.draw.rect(surface, player2_color, pygame.Rect(x, y, 45, 45))

    for i in range(len(fallen_blocks)):
        if fallen_blocks[i][2] == "Player 1":
            pygame.draw.rect(surface, player1_color, pygame.Rect(fallen_blocks[i][0], fallen_blocks[i][1], 45, 45))
        else:
            pygame.draw.rect(surface, player2_color, pygame.Rect(fallen_blocks[i][0], fallen_blocks[i][1], 45, 45))

def move():
    global fall_switch
    global x
    global y

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_TAB:
                pygame.quit()
            
            if event.key == pygame.K_a:
                x -= 50
                if x < 0:
                    x=300


            elif event.key == pygame.K_d:
                x += 50
                if x > 300:
                    x=0


            elif event.key == pygame.K_s:
                fall_switch = 1




while True:
    if turn == "Player 1":
        title = player1_name+" - "+str(x)
    else:
        title = player2_name+" - "+str(x)

    pygame.display.set_caption(title)

    surface.fill((0, 0, 0))

    if fall_switch == 1:
        fall()
    else:
        move()

    win_checker()
    grid_update()


    draw()
    win_checker()


    pygame.display.update()
    sleep(0.05)

    
