import pygame
import time
import random
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Pygame First Game Project")
assets = ["asset/heart.png"]
#Player
player_x = 400
player_y = 550
#Ball
ball_x = random.randint(0,795)
ball_y = random.randint(0,450)
spawn = True
#Heart
heart_x = random.randint(0,745)
heart_y = random.randint(0,450)
heart_spawn = False
#Player Move Mechanics
move_left = False
move_right = False
#Ball Move Mechanics
ball_move_up = True
ball_move_down = False
ball_move_left = True
ball_move_right = False
ball_vel=0.5
#Values
skor = 0
lives = 3
pause = False
stop = False
main_menu = True
spawn_time = 0
font = pygame.font.Font("font/poxel-font.ttf",35)
fps =1300
ball_touch_count = 0
heart_box = False
while True:
    pygame.time.Clock().tick(fps)

    if skor >= 5:
        fps = fps*1.3
    if skor >= 15:
        fps = fps*1.3


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_ESCAPE:
                pause = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False
    #Player Controls
    if stop == False:
        if move_right:
            player_x += 1
        if move_left:
            player_x -= 1
        if player_x <= 4:
            player_x = 4
        if player_x >= 695:
            player_x = 695
        screen.fill((0,0,0))
        player = pygame.draw.rect(screen,(255,255,255),pygame.Rect(player_x,player_y,100,10))
        if spawn == True:
            ball = pygame.draw.rect(screen,(255,255,255),pygame.Rect(ball_x,ball_y,10,10))

        #Ball Movement
        if ball_move_left:
            ball_x -= ball_vel
            if ball_x <= 0:
                ball_move_left = False
                ball_move_right = True
        if ball_move_right:
            ball_x += ball_vel
            if ball_x >= 799:
                ball_move_left = True
                ball_move_right = False
        if ball_move_up:
            ball_y -= ball_vel
            if ball_y <= 0:
                ball_move_up = False
                ball_move_down = True
        if ball_move_down:
            ball_y += ball_vel
            if pygame.Rect.colliderect(player,ball):
                ball_move_down = False
                ball_move_up = True
                skor += 1
                spawn_time += 1
                ball_touch_count +=1
        if ball_y >= 600:
            spawn = False
            ball_y = random.randint(0,1)
            ball_x = random.randint(0,795)
            lives -= 1

        if ball_y <= 450:
            spawn = True

        if ball_touch_count >= 5:
            heart_spawn = True
        if ball_touch_count >= 7:
            heart_spawn = False
            ball_touch_count = 0
    #Heart
    heart = pygame.image.load(assets[0])
    if heart_spawn:
        heart_box = pygame.Rect(heart_x+25,heart_y+17,15,18)
        screen.blit(heart,(heart_x,heart_y))
        if pygame.Rect.colliderect(heart_box,ball):
            heart_x = random.randint(0,785)
            heart_y = random.randint(0,450)
            lives += 1
            heart_spawn = False
            ball_touch_count = 0
    draw_skor = font.render("Score: {} ".format(skor),True,(255,255,255))
    draw_lives = font.render("Live: {}".format(lives),True,(255,255,255))
    screen.blit(draw_skor,(0,0))
    screen.blit(draw_lives,(695,0))
    if lives <= 0:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause = False
        pos = pygame.mouse.get_pos()
        stop = True
        restrat_text = font.render(" Restrat",True,(255,255,255))
        quit_text = font.render("Quit",True,(255,255,255))
        restrat_text_rect = pygame.draw.rect(screen,(255,255,255),pygame.Rect(310,130,152,39),2)
        quit_text_rect = pygame.draw.rect(screen,(255,255,255),pygame.Rect(310,180,152,39),2)
        screen.blit(restrat_text,(310,130))
        screen.blit(quit_text,(350,180))
        if event.type == pygame.MOUSEBUTTONUP:
            if restrat_text_rect.collidepoint(pos):
                ball_x = random.randint(0,795)
                ball_y = random.randint(0,450)
                stop = False
                lives = 3
                skor = 0
            if quit_text_rect.collidepoint(pos):
                pygame.quit()
                sys.exit()

    if pause == True:
        stop = True
        continue_text = font.render("Continue",True,(255,255,255))
        quit_text = font.render("Quit",True,(255,255,255))
        continue_text_rect = pygame.draw.rect(screen,(255,255,255),pygame.Rect(310,130,152,39),2)
        quit_text_rect = pygame.draw.rect(screen,(255,255,255),pygame.Rect(310,180,152,39),2)

        screen.blit(continue_text,(310,130))
        screen.blit(quit_text,(350,180))
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            if continue_text_rect.collidepoint(pos):
                pause = False
                stop = False
            if quit_text_rect.collidepoint(pos):
                pygame.quit()
                sys.exit()

    pygame.display.update()
