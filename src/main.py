import pygame
from pygame.locals import *
from random import randint
from math import *

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

GROUND_COLOR = (17, 217, 63)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Evolution Simulator')

pygame.font.init()
font = pygame.font.SysFont('Arial', 15)
time = 0

class being(pygame.sprite.Sprite):
    def __init__(self, position, size):
        pygame.sprite.Sprite.__init__(self)

        self.color = (228, 240, 111)
        self.velocity = 5
        self.hungry = 0

        self.image = pygame.Surface((size, size))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        self.rect[0] = position[0]
        self.rect[1] = position[1]

        self.theta = pi/4
        self.walk = False    

    def update(self):
        if self.walk:
            self.rect[0] += cos(-self.theta)*self.velocity
            self.rect[1] += sin(-self.theta)*self.velocity


class food(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()

        self.rect[0] = position[0]
        self.rect[1] = position[1]
        

    def update(self):
        pass

        

population = pygame.sprite.Group()
population.add(being((100, 100), 25))

food_group = pygame.sprite.Group()

clock = pygame.time.Clock()
while True:
    clock.tick(50)
    screen.fill(GROUND_COLOR)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    if round(time, 2) % 10 == 0:
        food_group.add(food((randint(0, 600), randint(0, 600))))

    for ind in population.sprites():
        if len(food_group.sprites()) != 0:
            ind.walk = True 
            dist_values = []
            for fod in food_group.sprites():
                # TODO: code the distance
                dist_values.append(sqrt())

        else:
            ind.walk = False


    population.update()
    population.draw(screen)
    food_group.draw(screen)

    time += 0.1
    pygame.display.flip()
    pygame.display.update()
