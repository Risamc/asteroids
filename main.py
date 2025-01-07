from player import Player
import pygame
from constants import *

pygame.init()

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updatable, drawable)

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0

def game_loop():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		dt = clock.tick(60) / 1000

		screen.fill((0, 0, 0))

		for obj in updatable:
			obj.update(dt)

		for obj in drawable:
			obj.draw(screen)
		
		pygame.display.flip()
		
def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == '__main__':
	main()
	game_loop()
