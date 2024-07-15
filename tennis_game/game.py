import pygame
import random

pygame.init()

# Screen dimensions
width, height = 800, 600
sc = pygame.display.set_mode((width, height))

# Background and game over images
background_img = pygame.image.load("background.jpg")
gameover_img = pygame.image.load("gameover.jpg")

# Resize images if needed
background_img = pygame.transform.scale(background_img, (width, height))
gameover_img = pygame.transform.scale(gameover_img, (width, height))

# Sound effects
try:
    hit_sound = pygame.mixer.Sound("pointls.wav")
    miss_sound = pygame.mixer.Sound("vo1.wav")
except FileNotFoundError:
    print("Sound files not found. Make sure 'pointls.wav' and 'vo1.wav' are present in the working directory.")
    pygame.quit()
    exit()

# FPS settings
fps = 30
time = pygame.time.Clock()

# Score tracking
score1 = 0
score2 = 0

class Game:
    def __init__(self):
        self.game_over = False
    
    def update(self):
        pass
    
    def draw(self):
        if self.game_over:
            sc.blit(gameover_img, (0, 0))
            self.show_score(center=True)
        else:
            sc.blit(background_img, (0, 0))
            player1_group.draw(sc)
            player2_group.draw(sc)
            ball_group.draw(sc)
            self.show_score()

    def show_score(self, center=False):
        font = pygame.font.SysFont(None, 55)
        score_text = font.render(f"{score1} - {score2}", True, (255, 255, 255))
        if center:
            sc.blit(score_text, (width//2 - score_text.get_width()//2, height//2 - score_text.get_height()//2))
        else:
            sc.blit(score_text, (width//2 - score_text.get_width()//2, 20))

    def check_collision(self):
        global score1, score2
        if pygame.sprite.spritecollideany(ball, player1_group) or pygame.sprite.spritecollideany(ball, player2_group):
            ball.speed_x *= -1
            hit_sound.play()
        if ball.rect.left <= 0:
            score2 += 1
            miss_sound.play()
            self.reset_ball()
        if ball.rect.right >= width:
            score1 += 1
            miss_sound.play()
            self.reset_ball()
        if score1 >= 5 or score2 >= 5:
            self.game_over = True

    def reset_ball(self):
        ball.rect.center = (width // 2, height // 2)
        ball.speed_x = random.choice([-10, 10])
        ball.speed_y = random.choice([-10, 10])

class Player(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (50, 150))  # Resize the player paddle
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10
    
    def update(self, up_key, down_key):
        keys = pygame.key.get_pressed()
        if keys[up_key] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[down_key] and self.rect.bottom < height:
            self.rect.y += self.speed

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ball.png")
        self.image = pygame.transform.scale(self.image, (30, 30))  # Resize the ball
        self.rect = self.image.get_rect()
        self.rect.center = (width // 2, height // 2)
        self.speed_x = random.choice([-10, 10])
        self.speed_y = random.choice([-10, 10])
    
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.top <= 0 or self.rect.bottom >= height:
            self.speed_y *= -1

# Player and ball groups
player1_group = pygame.sprite.Group()
player1 = Player("1_player.png", 0, height // 2)
player1_group.add(player1)

player2_group = pygame.sprite.Group()
player2 = Player("2_player.png", width - 50, height // 2)
player2_group.add(player2)

ball_group = pygame.sprite.Group()
ball = Ball()
ball_group.add(ball)

game = Game()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game.game_over:
        player1.update(pygame.K_w, pygame.K_s)
        player2.update(pygame.K_UP, pygame.K_DOWN)
        ball_group.update()
        game.check_collision()
    
    game.draw()
    pygame.display.update()
    time.tick(fps)

pygame.quit()
