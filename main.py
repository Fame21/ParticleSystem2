import pygame
import math
import json
import sys
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
    """

    :param start: Кординаты 1 точки
    :param end:  Координаты 2 точки
    :return: Угол в градусах между прямой проходящей через [start,end] и горизонтальной прямой
    """
    vector = [start[0] - end[0], start[1] - end[1]]
    if vector[0] == 0:
        vector[0] = 1
    angle = -round(math.degrees(math.atan(vector[1] / vector[0])))
    if vector[0] > 0:
        return angle + 180
    else:
        return angle


def setupEmmiter():
    '''

    :return: Список с координатами эммитара и иглом испускания частиц
    '''
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
    '''
    Пользователь создаёт новую частицу и она сохраняется в файле \{login}\presets.json
    :return: None
    '''

    name = input("Введите название: ")
    size = int(input("Введите размер: "))
    lifespan = int(input("Введите продолжительность жизни: "))
    color = [R, G, B] = [int(x) for x in input("Введите цвет в формате rgb - '255 0 255' : ").split()]

    # imgsrc = None

    shape = input("Введите форму(cir,tri,sqr,star): ")

    newParticle = {
        "name": name,
        "size": size,
        "lifespan": lifespan,
        "color": color,
        "shape": shape
    }
    directory = sys.argv[0][0:-7] + "Accounts\\" + loaderData[0]
    path = directory + "\\presets.json"

    oldPresets = {}
    with open(path) as presets:
        oldPresets = json.load(presets)
    oldPresets["particles"].append(newParticle)

    with open(path, "w") as presets:
        json.dump(oldPresets, presets)
    input("Частица сохранена! Нажмите 'Enter'")


def setupParticle():
    """
    Обработка создания/загрузки частиц
    :returns: Прототип объекта класса Particle или сообщение об ошибке
    """
    ans = input("Хотите создать новую частицу? [Y/N]\n").upper()

    directory = sys.argv[0][0:-7] + "Accounts\\" + loaderData[0]
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
    testParticle = setupParticle() # Установка позиции и угла испускания для эммитера
    start = setupEmmiter() # Установка эммитера
    testEmmiter = Emmiter(testParticle, # Прото-Частица
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