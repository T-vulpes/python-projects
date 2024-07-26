import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))

background = pygame.image.load('background.jpg')

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('player.png')
playerImg = pygame.transform.scale(playerImg, (100, 100)) 
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 20

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyImg[i] = pygame.transform.scale(enemyImg[i], (60, 60))  # Resim boyutunu ayarlayın
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(2)  # Düşmanların hızını ayarlayın
    enemyY_change.append(40)

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletImg = pygame.transform.scale(bulletImg, (32, 32))  # Resim boyutunu ayarlayın
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"  # "ready" - you can't see the bullet, "fire" - the bullet is moving

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)
win_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def win_text():
    win_text = win_font.render("KAZANDIN", True, (255, 255, 255))
    screen.blit(win_text, (250, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    return distance < 27

# Game Loop
running = True
clock = pygame.time.Clock()  # Hız kontrolü için saat ekleyin

while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Checking for boundaries of spaceship so it doesn't go out of bounds
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    all_enemies_defeated = True
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            running = False
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 2  # Düşmanların hızını ayarlayın
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -2  # Düşmanların hızını ayarlayın
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        if enemyY[i] < 2000:  # Düşmanın yenilip yenilmediğini kontrol edin
            all_enemies_defeated = False

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)

    if all_enemies_defeated:
        win_text()
        running = False

    pygame.display.update()
    clock.tick(60)  # Oyun hızını ayarlayın (60 FPS)
