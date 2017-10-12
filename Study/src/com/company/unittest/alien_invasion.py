'''
Created on Oct 6, 2017

@author: Sku293
'''
import sys

import pygame
from ship import Ship
def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Suresh Alien Invasion")
    bg_color = (230, 230, 230)
    screen.fill(bg_color)
    ship = Ship(screen)
    # Start the main loop for the game.
    while True:          # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            # Make the most recently drawn screen visible.
            ship.blitme()
            pygame.display.flip()
run_game()