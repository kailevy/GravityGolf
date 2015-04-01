"""
Patrick Huston, Kai Levy
Mechanics with Zhenya, Spring 2015
Physics-Enhanced Mini Golf
"""

import pygame
import os
import numpy as np

# Screen dimensions
SCREEN_WIDTH  = 800
SCREEN_HEIGHT = 600

# Colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
RED      = ( 255,   0,   0)
GREEN    = (   0, 255,   0)

CURR_DIR = os.path.dirname(os.path.realpath(__file__))

# Define global tiled level arrays
level0 = np.array(
   [(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)])

class GolfModel():
    """Represents the game state"""
    def __init__(self, width, height):
        self.levels = all_levels
        self.current_level = 0
        self.width = width
        self.height = height
        self.tiles = pygame.sprite.Group()
        self.level = Level(self.levels[current_level])

    def update(self, delta_t):
    	self.ball.update(delta_t)

class GolfView():
    """Represents the view of the game"""
    def __init__(self, model, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.model = model

    def draw(self):
        """ Redraw the full game window """
        self.screen.fill((0,0,0)) #Set background to black
        self.model.ball.draw(self.screen)
        self.model.level.draw(self.screen)
        pygame.display.update()

class GolfController():
	""" Represents controller for Gravity Golf Game """
	def __init__(self, model):
		self.model = model

	def process_events(self):
		done = False
		pygame.event.pump()


		# for event in pygame.event.get():

			#Define events that game elements should respond to

		return done

class GolfGame():
    """Runs the game"""
    def __init__(self):
        self.model = GolfModel(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.view = GolfView(self.model, SCREEN_WIDTH, SCREEN_HEIGHT)
        self.controller = GolfController(self.model)
        self.clock = pygame.time.Clock()

    def run(self):
    	""" Run the game """
    	last_ticks = 0.0
    	done = False

    	while not done:
    		t = pygame.time.get_ticks() # Get current time
    		dt = (t - last_ticks) / 1000.0
    		last_ticks = t

    		done = self.controller.process_events() # Process all events
    		self.model.update(dt) # Update model based on events
    		self.view.draw() # Draw view

    		self.clock.tick(25) # Change in time


class Ball(pygame.sprite.Sprite):
    """Represents a ball, for extension into: game ball, gravity ball..."""
    def __init__(self, pos_x, pos_y, tiles):
        """ Initialize a ball at specified position pos_x, pos_y """

        pygame.sprite.Sprite.__init__(self)

        #Set relevant state variables

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = 0
        self.vel_y = 0
        self.acc_x = 0
        self.acc_y = 0

        self.tiles = tiles
        self.onGround = False

        self.image = pygame.image.load('img/mario.png')
        self.rect = self.image.get_rect()

        self.rect = self.rect.move(pos_x, pos_y)

    def draw(self, screen):
        # Draw ball with transparent background - convert_alpha
        screen.blit(self.image.convert_alpha(), self.rect)

    def update(self, dt):
        """ Update ball due to passage of time """

        # x-axis updates and collisions
        self.rect.x += self.x_vel*dt
        self.collide(self.x_vel, 0)

        # y-axis updates and collisions


class Level(pygame.sprite.Sprite):
	""" Represents a level """
	def __init__(self, map):
		pygame.sprite.Sprite.__init__(self)
		self.map = map
		self.tiles = pygame.sprite.Group()

		#Creates map of tiles from inputted np array
		for row in xrange(len(self.map)):
			for x in xrange(len(self.map[row])):
                if self.map[row][x] == 0:
                    tile = FrictionTile(x*50, row*50)
                    self.tiles.add(tile)
				#For each element in array, create relevant tile

				#TODO: define all tile class(es)

	def draw(self, screen):
		for tile in self.tiles:
			tile.draw(screen)

class Tile(pygame.sprite.Sprite):
    """Represents a tile, for extension into: friction tile, wall tile, acceleration tile..."""
    def __init__(self, x_pos, y_pos):
    	pygame.sprite.Sprite.__init__(self)

    	self.x_pos = x_pos
    	self.y_pos = y_pos

    	self.image = pygame.image.load('img/wallTile.png')
    	self.rect = self.image.get_rect()

    	self.rect = self.rect.move(self.x_pos, self.y_pos)

	def draw(self, screen):
		screen.blit(self.image.convert_alpha(), self.rect)

class AccelTile(Tile):
	def __init__(self, x_pos, y_pos, acceleration):
		Tile.__init__(self, x_pos, y_pos)
		if acceleration == -1:
			self.image = pygame.image.load('img/negAccelTile')
		if acceleration == 1:
			self.image = pygame.image.load('img/posAccelTile')
		if acceleration == 3:
			self.image = pygame.image.load('img/rightAccelTile')
		if acceleration == 4:
			self.image = pygame.image.load('img/leftAccelTile') 

class FrictionTile(Tile):
    def __init__(self, x_pos, y_pos):
        Tile.__init__(self, x_pos, y_pos)
        self.image = pygame.image.load('img/frictionTile')
        

if __name__ == '__main__':
    pass