#Goal Scoring Game
import pygame
import random

pygame.init()

width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("goal scoring game")

player_img = pygame.image.load('player.png')
ball_img = pygame.image.load('ball.png')
goal_img = pygame.image.load('goal.png')
bg_img = pygame.image.load('background.jpg')

player_img = pygame.transform.scale(player_img, (80, 80))
ball_img = pygame.transform.scale(ball_img, (30, 30))
goal_img = pygame.transform.scale(goal_img, (250, 150)) 
bg_img = pygame.transform.scale(bg_img, (width, height))

white = (255, 255, 255)

player_x = width // 2 - 40
player_y = height - 100
player_speed = 7

ball_x = player_x + 25
ball_y = player_y - 30
ball_speed_x = 0
ball_speed_y = 0

goal_x = width // 2 - 125  
goal_y = 50

running = True
goal_scored = False
score = 0

while running:
    pygame.time.delay(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
        if ball_speed_y == 0:  
            ball_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - 80:
        player_x += player_speed
        if ball_speed_y == 0:  
            ball_x += player_speed
    if keys[pygame.K_SPACE] and ball_speed_y == 0:
        ball_speed_y = -10
        ball_speed_x = random.randint(-3, 3)
    
    # Update ball position
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    
    if (goal_x <= ball_x <= goal_x + 250) and (goal_y <= ball_y <= goal_y + 150):
        goal_scored = True
        score += 1
        ball_speed_x = 0
        ball_speed_y = 0
        ball_x = player_x + 25
        ball_y = player_y - 30
        goal_x = random.randint(0, width - 250)
        goal_y = 50
    
    if ball_y < 0 or ball_x < 0 or ball_x > width or ball_y > height:
        ball_x = player_x + 25
        ball_y = player_y - 30
        ball_speed_x = 0
        ball_speed_y = 0
        goal_x = random.randint(0, width - 250)
        goal_y = 50
        goal_scored = False

    win.blit(bg_img, (0, 0))
    
    win.blit(goal_img, (goal_x, goal_y))
    
    win.blit(player_img, (player_x, player_y))
    
    win.blit(ball_img, (ball_x, ball_y))
    
    font = pygame.font.Font(None, 36)
    text = font.render(f'Score: {score}', 1, white)
    win.blit(text, (10, 10))
    
    pygame.display.update()

pygame.quit()
