import pygame
import math
import json

import Loader

from Const import *

from Classes.Particle import Particle
from Classes.Emmiter import Emmiter

pygame.init()

pygame.display.set_caption('Particle System')
screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

print("LOADED")


def getAngle(start, end):
    vector = [start[0] - end[0], start[1] - end[1]]
    if vector[0] == 0:
        vector[0] = 1
    angle = -round(math.degrees(math.atan(vector[1] / vector[0])))
    if vector[0] > 0:
        return angle + 180
    else:
        return angle


def setupEmmiter():
    checking = True
    gottem = False
    start = [None, None, None]

    while checking:

        for i in pygame.event.get():
            if i.type == pygame.MOUSEBUTTONDOWN and not gottem:
                start[0] = pygame.mouse.get_pos()
                gottem = True
            elif i.type == pygame.MOUSEBUTTONUP:
                start[1] = pygame.mouse.get_pos()
                checking = False
        if start[0]:
            screen.fill(BLACK)
            pygame.draw.line(screen, WHITE, start[0], pygame.mouse.get_pos(), 3)
            clock.tick(FPS)
            pygame.display.update()
    start[2] = round(math.hypot(abs(start[0][0] - start[1][0]),
                                abs(start[0][1] - start[1][1])))
    start[1] = getAngle(start[0], start[1])
    # print(start)
    return start


def createParticle():

    name = input("Enter name: ")

    size = int(input("Enter size: "))

    lifespan = int(input("Enter lifespan: "))

    color = [R, G, B] = [int(x) for x in input("Enter 'R G B': ").split()]


    shape = input("Enter shape(cir,tri,sqr,star): ")

    newParticle = {
        "name": name,
        "size": size,
        "lifespan": lifespan,
        "color": color,
        "shape": shape
    }

    directory = "C:\\Users\\Admin\\Desktop\\ParticleSystem2\\Accounts\\" + loaderData[0]
    path = directory + "\\presets.json"

    oldPresets = {}
    with open(path) as presets:
        oldPresets = json.load(presets)
    oldPresets["particles"].append(newParticle)

    with open(path, "w") as presets:
        json.dump(oldPresets, presets)
    input("Частица сохранена! Press 'Enter'")


def setupParticle():
    ans = input("Хотите создать новую частицу? [Y/N]\n").upper()

    directory = "C:\\Users\\Admin\\Desktop\\ParticleSystem2\\Accounts\\" + loaderData[0]
    path = directory + "\\presets.json"

    if ans == "Y":
        createParticle()
        return setupParticle()
    elif ans == "N":
        with open(path) as presets:
            data = json.load(presets)
            print("Список доступных частиц: ")
            for p in data["particles"]:
                print("#%d: %s" % (data["particles"].index(p), p))
            index = int(input("Выберите номер: ").lower())
            loadedParticle = data["particles"][index]
            # print(loadedParticle)
            particle = Particle(loadedParticle["size"],
                                loadedParticle["lifespan"],
                                loadedParticle["color"],
                                loadedParticle["shape"])
            return particle
    return print("ERROR")


def main():
    # horse = pygame.image.load("img\\horse_new.png")
    # bg = pygame.image.load('img\\bg.png')

    testParticle = setupParticle()
    start = setupEmmiter()
    testEmmiter = Emmiter(testParticle, # Частица
                          start[0], # Стартовая позиция
                          start[1] + 10, # Угол 1
                          start[1] - 10, # Угол 2
                          20, # Скорость
                          1.1,
                          None) # Гравитация


    isRunning = True
    # главный цикл
    while isRunning:
        # Кадры в секунду
        pygame.time.delay(17*2)
        # screen.blit(bg, (0, 0))
        screen.blit(background, (0, 0))
        # screen.blit(horse, (500, 400))
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print(pygame.mouse.get_pos())
                pass
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass
        testEmmiter.emmit_new()
        # --------------
        testEmmiter.emmit_old()
        # --------------
        pygame.display.update()

# ----------------------------------------------- #


loaderData = Loader.launch()

if __name__ == "__main__":
    main()