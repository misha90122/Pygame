import pygame
import random
import os
from pygame.constants import K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

# Constants
FPS = pygame.time.Clock()
HEIGHT = 800
WIDTH = 1200
COLOR_BLACK = (0, 0, 0)
COLOR_RAD = (225, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREEN = (1, 80, 32)
PLAYER_MOVE_SPEED = 5
FONT = pygame.font.SysFont("Verdana", 20)

# Set up display
main_display = pygame.display.set_mode((WIDTH, HEIGHT))


# Background
bg = pygame.transform.scale(pygame.image.load("background.png"), (WIDTH, HEIGHT))
bg_X1 = 0
bg_X2 = bg.get_width()
bg_move = 3

# Set up player
player = pygame.image.load("player.png").convert_alpha()
player_rect = player.get_rect(topleft=(0, HEIGHT // 2))

IMAGE_PATH = "goose"
PLAYER_IMAGES = os.listdir(IMAGE_PATH)

# Set up bonuses
bonus_images = [pygame.transform.scale(pygame.image.load("bonus.png"), (89.5, 149))]
bonus_rects = []
bonus_speed = 3


# ENEMY
def create_enemy():
    """Створює нового ворога з випадковим положенням та швидкістю руху."""
    enemy = pygame.transform.scale(pygame.image.load("enemy.png"), (102.5, 36))
    enemy_rect = enemy.get_rect()
    enemy_rect.x = WIDTH
    enemy_rect.y = random.randint(100, HEIGHT - 100)
    enemy_move = [random.randint(-8, -4), 0]
    return [enemy, enemy_rect, enemy_move]




# BONUS
def create_bonus():
    """Створює новий бонус з випадковим зображенням, положенням та швидкістю руху."""
    bonus_image = random.choice(bonus_images)
    bonus_rect = bonus_image.get_rect()
    bonus_rect.x = random.randint(50, WIDTH - 50)
    bonus_rect.y = 50
    bonus_speed = random.randint(4, 8)
    return [bonus_image, bonus_rect, bonus_speed]


CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)
enemies = []

CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 6000)
bonuses = []
CHANGE_IMAGE = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMAGE, 250)

score = 0
image_index = 0

# Main game loop
playing_game = True
while playing_game:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing_game = False
        elif event.type == CREATE_ENEMY:
            enemies.append(create_enemy())
        elif event.type == CREATE_BONUS:
            bonuses.append(create_bonus())
        if event.type == CHANGE_IMAGE:
            player = pygame.image.load(os.path.join(IMAGE_PATH, PLAYER_IMAGES[image_index])).convert_alpha()
            image_index += 1
            if image_index >= len(PLAYER_IMAGES):
                image_index = 0

    # Background
    bg_X1 -= bg_move
    bg_X2 -= bg_move

    if bg_X1 < -bg.get_width():
        bg_X1 = bg.get_width()

    if bg_X2 < -bg.get_width():
        bg_X2 = bg.get_width()

    main_display.blit(bg, (bg_X1, 0))
    main_display.blit(bg, (bg_X2, 0))

    # Moving the player
    keys = pygame.key.get_pressed()
    player_movement = [0, 0]
    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_movement[1] = PLAYER_MOVE_SPEED
    if keys[K_RIGHT] and player_rect.right < WIDTH:
        player_movement[0] = PLAYER_MOVE_SPEED
    if keys[K_LEFT] and player_rect.left > 0:
        player_movement[0] = -PLAYER_MOVE_SPEED
    if keys[K_UP] and player_rect.top > 0:
        player_movement[1] = -PLAYER_MOVE_SPEED
    player_rect = player_rect.move(player_movement)

    # Remove enemies that are offscreen
    for enemy in enemies:
        if enemy[1].left < 0:
            enemies.remove(enemy)

    # Clear bonuses if more than 10
    for bonus in bonuses:
        if bonus[1].top > HEIGHT:
            bonuses.remove(bonus)

    # Update enemies
    for enemy in enemies:
        enemy[1].x += enemy[2][0]
        enemy[1].y += enemy[2][1]
        main_display.blit(enemy[0], enemy[1])

        if player_rect.colliderect(enemy[1]):
            playing_game = False

    # Update bonuses
    for bonus in bonuses:
        bonus[1].y += bonus[2]
        main_display.blit(bonus[0], bonus[1])

        if player_rect.colliderect(bonus[1]):
            score += 1
            bonuses.remove(bonus)

    # Draw screen
    main_display.blit(FONT.render(str(score), True, COLOR_RAD), (WIDTH - 50, 20))
    main_display.blit(player, player_rect)

    pygame.display.flip()

    # Control framerate
    FPS.tick(60)

pygame.quit()
