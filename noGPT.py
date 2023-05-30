import pygame
import random
from pygame.constants import K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

# Constants
FPS = pygame.time.Clock()
HEIGHT = 800
WIDTH = 1200
COLOR_BLACK = (0, 0, 0)
COLOR_RAD = (225, 0, 0)
PLAYER_MOVE_UP = [0, -1]
PLAYER_MOVE_DOWN = [0, 1]
PLAYER_MOVE_RIGHT = [1, 0]
PLAYER_MOVE_LEFT = [-1, 0]

# Set up display
main_display = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up player
player = pygame.image.load("player.png")
player_rect = player.get_rect()


# ENEMY
def create_enemy():
    enemy = pygame.image.load("enemy.png")
    enemy_size = (30, 30)
    # enemy = pygame.Surface(enemy_size)
    # enemy.fill(COLOR_RAD)
    enemy_rect = pygame.Rect(WIDTH, random.randint(0, HEIGHT), *enemy_size)
    enemy_move = [random.randint(-6, -1), 0]
    return [enemy, enemy_rect, enemy_move]


CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)
enemyes = []

# Main game loop
playing_game = True
while playing_game:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing_game = False
        if event.type == CREATE_ENEMY:
            enemyes.append(create_enemy())

    # Move player
    keys = pygame.key.get_pressed()

    if keys[K_DOWN] and player_rect.bottom < HEIGHT:
        player_rect = player_rect.move(PLAYER_MOVE_DOWN)

    if keys[K_RIGHT] and player_rect.right < WIDTH:
        player_rect = player_rect.move(PLAYER_MOVE_RIGHT)

    if keys[K_LEFT] and player_rect.left > 0:
        player_rect = player_rect.move(PLAYER_MOVE_LEFT)

    if keys[K_UP] and player_rect.top > 0:
        player_rect = player_rect.move(PLAYER_MOVE_UP)

    # Draw screen
    main_display.fill(COLOR_BLACK)

    # ENEMY MOVE
    for enemy in enemyes:
        enemy[1] = enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])

    main_display.blit(player, player_rect)
    pygame.display.flip()
    print(len(enemyes))

    for enemy in enemyes:
        if enemy[1].left < 0:
            enemyes.pop(enemyes.index(enemy))

    # Control framerate
    FPS.tick(400)
