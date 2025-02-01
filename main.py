import pygame
import os

from constants import *
from player import Player

os.environ["LIBGL_ALWAYS_INDIRECT"] = "1"
os.environ["SDL_AUDIODRIVER"] = "dummy"
os.environ["DISPLAY"] = "host.docker.internal:0"


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    # run the game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        player.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
