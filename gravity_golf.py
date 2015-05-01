"""
Patrick Huston, Kai Levy
Mechanics with Zhenya, Spring 2015
Physics-Enhanced Mini Golf
"""

import pygame
import os
import numpy as np
import math

# Screen dimensions
SCREEN_WIDTH  = 1200
SCREEN_HEIGHT = 800

# Colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
RED      = ( 255,   0,   0)
GREEN    = (   0, 255,   0)

CURR_DIR = os.path.dirname(os.path.realpath(__file__))

# Define global tiled level arrays
level0 = np.array(
   [(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)])

level0 = np.array(
   [(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 0, 0, 4, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1),
    (1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 1),
    (1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1),
    (1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)])

all_levels = [level0]

class GolfModel():
    """Represents the game state"""
    def __init__(self, width, height):
        self.levels = all_levels
        self.current_level = 0
        self.width = width
        self.height = height
        self.level = Level(self.levels[self.current_level])
        self.ball = Ball(400, 400, self.level.tiles, self.level.planets)

    def update(self, delta_t):
    	self.ball.update(delta_t)

class GolfView():
    """Represents the view of the game"""
    def __init__(self, screen, model, controller, width, height):
        pygame.init()
        self.screen = screen
        self.model = model
        self.controller = controller

    def draw(self):
        """ Redraw the full game window """
        self.screen.fill((0,0,0)) #Set background to black
        self.model.level.draw(self.screen)
        self.model.ball.draw(self.screen)
        if self.controller.initialized and self.controller.mouse_press:
            pygame.draw.line(self.screen, WHITE, (self.controller.initx,self.controller.inity), 
                (self.controller.mx, self.controller.my))   
        pygame.display.update()

class GolfController():
    """ Represents controller for Gravity Golf Game """
    def __init__(self, model, screen):
        self.model = model
        self.mouse_press = False
        self.ball = self.model.ball
        self.screen = screen
        self.initx = 0
        self.inity = 0
        self.initialized = False
        self.mx = 0
        self.my = 0
        self.velocity = (0, 0)

    def process_events(self):
        done = False
        pygame.event.pump
        if not self.ball.moving:
            for events in pygame.event.get():
                self.mouse_press = pygame.mouse.get_pressed()[0]
                self.mx = pygame.mouse.get_pos()[0]
                self.my = pygame.mouse.get_pos()[1]
                if self.mouse_press and not self.initialized:
                        self.initx = self.ball.rect.x + 7   #adjust to make line go from center of circle
                        self.inity = self.ball.rect.y + 7   #adjust to make line go from center of circle
                        self.initialized = True
                if not pygame.mouse.get_pressed()[0] and self.initialized:
                    #get velocity based off of mouse movement
                    self.velocity = ( - (self.mx - self.initx), - (self.my - self.inity))
                else:
                    self.velocity = (0, 0)
                vx = self.velocity[0]
                vy = self.velocity[1]
                if (vx != 0 or vy != 0):
                    self.ball.putt(vx*3,vy*3)   #adjust to make hit harder
                    self.initialized = False             
                vx = 0
                vy = 0
        return done

class GolfGame():
    """Runs the game"""
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.model = GolfModel(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.controller = GolfController(self.model, self.screen)
        self.view = GolfView(self.screen, self.model, self.controller, SCREEN_WIDTH, SCREEN_HEIGHT)
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

            self.clock.tick(30) # Change in time


class Ball(pygame.sprite.Sprite):
    """Represents a ball, for extension into: game ball, gravity ball..."""
    def __init__(self, pos_x, pos_y, tiles, planets):
        """ Initialize a ball at specified position pos_x, pos_y """

        pygame.sprite.Sprite.__init__(self)

        #Set relevant state variables
        self.vel_x = 0 #20.0
        self.vel_y = 0 #20.0
        self.moving = False

        self.hit_count = 0

        self.tiles = tiles
        self.planets = planets

        self.image = pygame.image.load('img/ball.png')
        self.rect = self.image.get_rect()

        self.rect = self.rect.move(pos_x, pos_y)

    def putt(self, vx, vy):
        self.vel_x = vx
        self.vel_y = vy
        self.moving = True
        self.hit_count += 1

    def draw(self, screen):
        # Draw ball with transparent background - convert_alpha
        screen.blit(self.image.convert_alpha(), self.rect)

    def update(self, dt):
        """ Update ball due to passage of time """


        if (math.sqrt((self.vel_x)**2 + (self.vel_y)**2)) < 35:
            self.vel_x = 0
            self.vel_y = 0
            self.moving = False


        # x-axis updates and collisions
        self.rect.x += self.vel_x *dt
        self.collide(self.vel_x, 0, dt)

        # y-axis updates and collisions
        self.rect.y += self.vel_y*dt
        self.collide(0, self.vel_y, dt)

        self.gravitate(self.vel_x, self.vel_y, dt)

    def collide(self, vel_x, vel_y, delta_t):
        """ Handle collisions between ball and walls """

        for tile in self.tiles:

            if pygame.sprite.collide_rect(self, tile):
                if isinstance(tile, ExitTile) and (math.sqrt(vel_x**2 + vel_y**2) < 100):
                    self.vel_x = 0
                    self.vel_y = 0

                if self.vel_x != 0 and isinstance(tile, FrictionTile):
                    self.vel_x *= tile.acceleration

                if self.vel_y != 0 and isinstance(tile, FrictionTile):
                    self.vel_y *= tile.acceleration


                if vel_x > 0 and isinstance(tile, WallTile):
                    self.rect.right = tile.rect.left
                    self.vel_x *= -1

                if vel_x < 0 and isinstance(tile, WallTile):
                    self.rect.left = tile.rect.right
                    self.vel_x *= -1

                if vel_y > 0 and isinstance(tile, WallTile):
                    self.rect.bottom = tile.rect.top
                    self.vel_y *= -1

                if vel_y < 0 and isinstance(tile, WallTile):
                    self.rect.top = tile.rect.bottom
                    self.vel_y *= -1

    def gravitate(self, vel_x, vel_y, delta_t):
        for planet in self.planets:
            diff_x = self.rect.center[0] - planet.rect.center[0]
            diff_y = self.rect.center[1] - planet.rect.center[1]

            diff_total = math.sqrt(diff_x**2 + diff_y**2)

            if (diff_total < 100):
                self.vel_x -= 3*diff_x/(math.sqrt(abs(diff_x))+.1)
                self.vel_y -= 3*diff_y/(math.sqrt(abs(diff_y))+.1)

            # print diff_x, diff_y

class Level(pygame.sprite.Sprite):
    """ Represents a level """
    def __init__(self, map):
        pygame.sprite.Sprite.__init__(self)
        self.map = map
        self.tiles = pygame.sprite.Group()
        self.planets = pygame.sprite.Group()

		#Creates map of tiles from inputted np array
        for row in xrange(len(self.map)):
            for x in xrange(len(self.map[row])):
                #For each element in array, create relevant tile
                if self.map[row][x] == 0:
                    tile = FrictionTile(x*50, row*50)
                    self.tiles.add(tile)
                if self.map[row][x] == 1:
                    tile = WallTile(x*50, row*50)
                    self.tiles.add(tile)
                if self.map[row][x] == 2:
                    tile = FrictionTile(x*50, row*50)
                    self.tiles.add(tile)
                    exittile = ExitTile(x*50, row*50)
                    self.tiles.add(exittile)
                if self.map[row][x] == 3:
                    tile = FrictionTile(x*50, row*50)
                    self.tiles.add(tile)
                    planet = Planet(x*50, row*50)
                    self.planets.add(planet)
                if self.map[row][x] == 4:
                    tile = WallTile(x*50, row*50)
                    self.tiles.add(tile)
                    planet = Planet(x*50, row*50)
                    self.planets.add(planet)

    def draw(self, screen):
        for tile in self.tiles:
            tile.draw(screen)

        for planet in self.planets:
            planet.draw(screen)

class Tile(pygame.sprite.Sprite):
    """Represents a tile, for extension into: friction tile, wall tile, acceleration tile..."""
    def __init__(self, x_pos, y_pos):
    	pygame.sprite.Sprite.__init__(self)

    	self.x_pos = x_pos
    	self.y_pos = y_pos

    def draw(self, screen):
        screen.blit(self.image.convert_alpha(), self.rect)

class FrictionTile(Tile):
    """Represents regular floor tile that has a friction"""
    def __init__(self, x_pos, y_pos):
        Tile.__init__(self, x_pos, y_pos)

        self.acceleration = .99

        self.image = pygame.image.load("img/frictionTile.png")
        self.rect = self.image.get_rect()

        self.rect = self.rect.move(self.x_pos, self.y_pos)

class WallTile(Tile):
    """ Represents a wall tile that the golf ball will collide with """
    def __init__(self, x_pos, y_pos):
        Tile.__init__(self, x_pos, y_pos)

        self.image = pygame.image.load('img/wallTile.png')
        self.rect = self.image.get_rect()

        self.rect = self.rect.move(self.x_pos, self.y_pos)

class AccelTile(Tile):
    def __init__(self, x_pos, y_pos, acceleration):
        Tile.__init__(self, x_pos, y_pos)
        if acceleration == 0:
            self.image = pygame.image.load('img/negAccelTile')
        if acceleration == 1:
            self.image = pygame.image.load('img/posAccelTile')
        if acceleration == 2:
            self.image = pygame.image.load('img/rightAccelTile')
        if acceleration == 3:
            self.image = pygame.image.load('img/leftAccelTile') 

        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x_pos, self.y_pos)

class ExitTile(Tile):
    def __init__(self, x_pos, y_pos):
        Tile.__init__(self, x_pos, y_pos)
        self.image = pygame.image.load('img/exitTile.png')
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x_pos, self.y_pos)        

class Planet(pygame.sprite.Sprite):

    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)

        self.x_pos = x_pos
        self.y_pos = y_pos

        self.image = pygame.image.load('img/planet.png')
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x_pos, self.y_pos)

    def draw(self, screen):
        screen.blit(self.image.convert_alpha(), self.rect)


if __name__ == '__main__':
    golf = GolfGame()
    golf.run()