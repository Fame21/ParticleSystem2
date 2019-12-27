# import math
import pygame
import Const
from math import *
from random import randrange


def mapper(value, istart, istop, ostart, ostop):
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))


screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()



class Particle:
    def __init__(self, size, lifeSpan, color, shape):
        self.pos = None
        self.vel = None
        self.size = size
        self.sizeMax = size
        self.lifeSpan = lifeSpan
        self.lifeSpanMax = lifeSpan
        self.color = color
        self.shape = shape
        self.grav = None
        self.pic_angle = 0
        self.pic = pygame.image.load("img\\apple-var\\%s.png" % randrange(1,9))

    def draw(self):
        if self.shape == "cir":
            pygame.draw.circle(screen, self.color, self.pos, self.size)
        else:
            points = self.getPoints()
            pygame.draw.polygon(screen, self.color, points)
    def update(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        self.vel[1] = round(self.vel[1] + self.grav)

        self.size = round(mapper(self.lifeSpan, 0, self.lifeSpanMax, 0, self.sizeMax))

        if self.pos[0] > 800 + self.size or self.pos[0] < 0 - self.size:
            self.lifeSpan = 0
        if self.pos[1] > 600 + self.size or self.pos[1] < 0 - self.size:
            self.lifeSpan = 0

        # if self.lifeSpan:
        #     self.lifeSpan -= 1


    def getPoints(self):
        points = []
        numPoints = 0
        angle = 0
        if self.shape == "tri":
            numPoints = 3
            angle = radians(120)
        elif self.shape == "sqr":
            numPoints = 4
            angle = radians(90)
            # print(angle)
        elif self.shape == "star":
            numPoints = 5
            angle = radians(72)

        for ang in range(numPoints):
            x_ = self.pos[0] + cos((ang)*angle)*self.size
            y_ = self.pos[1] + sin((ang)*angle)*self.size
            points.append((round(x_),round(y_)))
        return points

