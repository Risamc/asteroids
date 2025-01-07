from player import Player
import player
import pygame
from constants import *
from circleshape import CircleShape

pygame.init()

player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0

def game_loop():
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		screen.fill((0, 0, 0))
		player.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000
		player.update(dt)
		

def main():
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == '__main__':
	main()
	game_loop()
