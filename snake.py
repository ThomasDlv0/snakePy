import pygame, random, time
from pygame.examples.moveit import HEIGHT
from pygame.examples.scrap_clipboard import screen
from pygments.styles.rainbow_dash import WHITE

# Initialisation de pygame
pygame.init()

# Definition des constantes
WIDTH, HEIGHT = 720, 480
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Création de la fenêtre
screen = pygame.display.set_mode(WIDTH, HEIGHT)
pygame.display.set_caption("Snake")

# Image par secondes
fps = pygame.time.Clock()


# Taille de segment du serpent
segment_size = 10

# Position, direction du serpent
snake_position = [100, 50]
direction = "RIGHT"
change_to = direction


# Variable globales
snake_body = [
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50],
]
fruit_position = [
    random.randrange(1, (WIDTH // 10)) * 10,
    random.randrange(1, (HEIGHT // 10)) * 10,
]

fruit_apparition = False
score = 0

# Boucle du jeu

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN" :
                change_to = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP" :
                change_to = "DOWN"
            elif event.key == pygame.K_RIGHT and direction != "LEFT" :
                change_to = "RIGHT"
            elif event.key == pygame.K_LEFT and direction != "RIGHT" :
                change_to = "LEFT"