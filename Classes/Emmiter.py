
import math
import pygame
import Const
import random
from Classes.Particle import Particle


clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))


def getRandomVector(srt, end, mult):
    vector = [0, 0]
    deg_ = math.radians(random.randint(end, srt))
    vector[0] = round(math.cos(deg_) * mult)
    vector[1] = -round(math.sin(deg_) * mult)
    # print(vector)
    return vector


def getAngle(start, end):
    vector = [start[0]-end[0], start[1]-end[1]]
    angle = -round(math.degrees(math.atan(vector[1] / vector[0])))
    if vector[0] > 0:
        return angle + 180
    else:
        return angle


class Emmiter:
    def __init__(self, protoPC, pos, degS, degE, vel, grav, pic):
        self.protoPC = protoPC
        self.protoPC.pos = (pos[0], pos[1])
        self.degS = degS
        self.degE = degE
        self.vel = vel
        self.pos = pos
        self.grav = grav
        self.PClist = []
        self.picture = pic

    def newPC(self):
        new = Particle(self.protoPC.size, self.protoPC.lifeSpan, self.protoPC.color, self.protoPC.shape)
        new.pos = [self.protoPC.pos[0], self.protoPC.pos[1]]
        new.vel = getRandomVector(self.degS, self.degE, self.vel)
        new.grav = self.grav
        # new.vel = (random.randint(-2, 2), random.randint(-2, 2))
        return new

    def check_horse(self, particle):
        shiftx = 15
        shifty = 10
        # pygame.draw.polygon(screen,(255,255,255),((600+shiftx,450+shifty),
        #                                           (660+shiftx,450+shifty),
                                                  # (660+shiftx,500+shifty),
                                                  # (600+shiftx,500+shifty)))
        if (particle.pos[0] > 550+shiftx and particle.pos[0] < 710+shiftx) and (particle.pos[1] > 400+shifty and particle.pos[1] < 600+shifty):
            return True
        return False

    def emmit_new(self):
        self.PClist.append(self.newPC())
    def emmit_old(self):
        for pc in reversed(self.PClist):
            pc.draw()
            # pc.pic = pygame.transform.rotate(pc.pic,pc.pic_angle)
            # pc.pic_angle +=1
            # if pc.pic_angle == 360:
            #     pc.pic_angle = 1
            # screen.blit(pc.pic, pc.pos)
            pc.update()
            # if self.check_horse(pc):
            #     self.PClist.remove(pc)
            if pc.lifeSpan <= 0:

                self.PClist.remove(pc)
        self.draw()



    def update(self):
        pass

    def draw(self):
        pygame.draw.circle(screen, Const.WHITE, self.pos, 10)
