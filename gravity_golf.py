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



level0 = np.array(
   [(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1),
    (1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 8, 8, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)])


# Define global tiled level arrays
level1 = np.array(
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

level2 = np.array(
   [(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 0, 0, 8, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 0, 0, 8, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 7, 7, 1, 6, 6, 1, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 0, 0, 4, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1),
    (1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 1),
    (1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1),
    (1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)])

congratulations = np.array(
   [(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1),
    (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1),
    (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1),
    (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1),
    (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1),
    (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1),
    (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1),
    (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1),
    (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1),
    (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)])
all_levels = [level0,level1,level2,congratulations]
NEXTLEVEL = pygame.USEREVENT + 1
next_level_event = pygame.event.Event(NEXTLEVEL, message="Next Level!")

class GolfModel():
    """Represents the game state"""
    def __init__(self, width, height):
        self.current_level = 0
        self.levels = all_levels
        self.width = width
        self.height = height
        self.level = Level(self.levels[self.current_level])
        self.start_coords = (200,650)
        self.ball = Ball(self.start_coords, self.level.tiles, self.level.planets)
        self.score = 0
        self.curr_score = 0

    def update(self, delta_t):
    	self.ball.update(delta_t)

    def next_level(self):
        self.current_level += 1
        self.level = Level(self.levels[self.current_level])        
        if self.current_level == 1:
            self.start_coords = (300,600)
        if self.current_level == 2:
            self.start_coords = (250,600)
        self.ball = Ball(self.start_coords, self.level.tiles, self.level.planets)
        self.curr_score = 0


class GolfView():
    """Represents the view of the game"""
    def __init__(self, screen, model, controller, width, height):
        pygame.init()
        self.screen = screen
        self.model = model
        self.controller = controller
        self.font = pygame.font.Font(CURR_DIR + '/visitor2.ttf', 80)

    def draw(self):
        """ Redraw the full game window """
        self.screen.fill((0,0,0)) #Set background to black
        self.model.level.draw(self.screen)
        self.model.ball.draw(self.screen)
        if self.controller.initialized and self.controller.mouse_press:
            pygame.draw.line(self.screen, WHITE, (self.controller.initx,self.controller.inity), 
                (self.controller.mx, self.controller.my))   
        self.draw_score()
        if self.model.current_level == 3:
            self.draw_congrats()
        pygame.display.update()

    def draw_score(self):
        """Draws score in corner"""
        self.score_surf = self.font.render("Total Score: " + str(self.model.score), False, BLACK)
        self.curr_score_surf = self.font.render("Strokes: " + str(self.model.curr_score), False, BLACK)
        self.screen.blit(self.curr_score_surf, (20, 70))
        self.screen.blit(self.score_surf, (20,20))

    def draw_congrats(self):
        self.gratz_surf = self.font.render("Game Complete!", False, BLACK)
        self.screen.blit(self.gratz_surf,(350,400))

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
            self.ball = self.model.ball
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    done = True
                if events.type == NEXTLEVEL:
                    self.model.next_level()
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
                    self.model.curr_score += 1 
                    if not self.model.current_level == 3:   
                        self.model.score += 1      
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
    def __init__(self, pos, tiles, planets):
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

        self.rect = self.rect.move(pos[0], pos[1])

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
                if isinstance(tile, ExitTile) and (math.sqrt(vel_x**2 + vel_y**2) < 120):
                    self.vel_x = 0
                    self.vel_y = 0
                    pygame.event.post(next_level_event)
                    self.tiles = []

                if self.vel_x != 0 and isinstance(tile, FrictionTile):
                    self.vel_x *= tile.acceleration

                if self.vel_y != 0 and isinstance(tile, FrictionTile):
                    self.vel_y *= tile.acceleration

                if isinstance(tile, AccelTile):
                    if tile.acceleration == 0:
                        self.vel_y += 5
                    if tile.acceleration == 1:
                        self.vel_y -= 5
                    if tile.acceleration == 2:
                        self.vel_x += 5
                    if tile.acceleration == 3:
                        self. vel_x -= 5

                # If golf ball moving right, reverse x velocity
                if vel_x > 0 and isinstance(tile, WallTile):
                    self.rect.right = tile.rect.left
                    self.vel_x *= -1

                # If golf ball moving left, reverse x velocity
                if vel_x < 0 and isinstance(tile, WallTile):
                    self.rect.left = tile.rect.right
                    self.vel_x *= -1

                # If golf ball moving up, reverse y velocity
                if vel_y > 0 and isinstance(tile, WallTile):
                    self.rect.bottom = tile.rect.top
                    self.vel_y *= -1

                # If golf ball moving down, reverse y velocity
                if vel_y < 0 and isinstance(tile, WallTile):
                    self.rect.top = tile.rect.bottom
                    self.vel_y *= -1

    def gravitate(self, vel_x, vel_y, delta_t):
        """Represents interaction with planets"""
        g_const = 300
        for planet in self.planets:
            diff_x = self.rect.center[0] - planet.rect.center[0]
            diff_y = self.rect.center[1] - planet.rect.center[1]

            diff_total = math.sqrt(diff_x**2 + diff_y**2)

            ratio_x = diff_x/diff_total
            ratio_y = diff_y/diff_total

            self.vel_x -= ratio_x*g_const*(planet.mass)/(((diff_total)**2)+.1)
            self.vel_y -= ratio_y*g_const*(planet.mass)/(((diff_total)**2)+.1)


class Level(pygame.sprite.Sprite):
    """ Represents a level """
    def __init__(self, map):
        pygame.sprite.Sprite.__init__(self)
        self.map = map
        self.tiles = pygame.sprite.Group()
        self.planets = pygame.sprite.Group()
        self.exits = pygame.sprite.Group()

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
                    self.exits.add(exittile)
                if self.map[row][x] == 3:
                    tile = FrictionTile(x*50, row*50)
                    self.tiles.add(tile)
                    planet = Planet(x*50, row*50, 60)
                    self.planets.add(planet)
                if self.map[row][x] == 4:
                    tile = WallTile(x*50, row*50)
                    self.tiles.add(tile)
                    planet = Planet(x*50, row*50, 60)
                    self.planets.add(planet)
                if self.map[row][x] == 5:
                    tile = WallTile(x*50, row*50)
                    self.tiles.add(tile)
                    title = TitleTile(x*50, row*50)
                    self.planets.add(title)
                if self.map[row][x] == 6:
                    tile = AccelTile(x*50, row*50, 0)
                    self.tiles.add(tile)
                if self.map[row][x] == 7:
                    tile = AccelTile(x*50, row*50, 1)
                    self.tiles.add(tile)
                if self.map[row][x] == 8:
                    tile = AccelTile(x*50, row*50, 2)
                    self.tiles.add(tile)
                if self.map[row][x] == 9:
                    tile = AccelTile(x*50, row*50, 3)
                    self.tiles.add(tile)



    def draw(self, screen):
        for tile in self.tiles:
            tile.draw(screen)

        for planet in self.planets:
            planet.draw(screen)
        # so that the exit is drawn last and definitely shows up
        for exit in self.exits:
            exit.draw(screen)

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
    """Represents a tile that will accelerate the ball in a certain direction"""
    def __init__(self, x_pos, y_pos, acceleration):
        Tile.__init__(self, x_pos, y_pos)
        self.acceleration = acceleration
        if acceleration == 0:
            self.image = pygame.image.load('img/downAccelTile.png')
        if acceleration == 1:
            self.image = pygame.image.load('img/upAccelTile.png')
        if acceleration == 2:
            self.image = pygame.image.load('img/rightAccelTile.png')
        if acceleration == 3:
            self.image = pygame.image.load('img/leftAccelTile.png') 

        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x_pos, self.y_pos)

class ExitTile(Tile):
    """Represent a the hole that send the player to the next level"""
    def __init__(self, x_pos, y_pos):
        Tile.__init__(self, x_pos, y_pos)
        self.image = pygame.image.load('img/exitTile.png')
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x_pos, self.y_pos)        

class TitleTile(Tile):
    """Tile that displays the title"""
    def __init__(self, x_pos, y_pos):
        Tile.__init__(self, x_pos, y_pos)
        self.image = pygame.image.load('img/title.png')
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x_pos, self.y_pos) 
        self.mass = 0        

class Planet(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, mass):
        """Represents a high mass object that attracts the ball towards it"""
        pygame.sprite.Sprite.__init__(self)

        self.x_pos = x_pos
        self.y_pos = y_pos

        self.mass = mass

        self.image = pygame.image.load('img/planet.png')
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(self.x_pos, self.y_pos)

    def draw(self, screen):
        screen.blit(self.image.convert_alpha(), self.rect)


if __name__ == '__main__':
    golf = GolfGame()
    golf.run()