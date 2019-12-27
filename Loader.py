import json
import os
from Coder import *

sudoClear = lambda: print('\n'*10)

def getPass(name):
    directory = "C:\\Users\\Admin\\Desktop\\ParticleSystem2\\Accounts\\" + name
    if os.path.exists(directory):
        path = "C:\\Users\\Admin\\Desktop\\ParticleSystem2\\Accounts\\" + name + "\\pass.txt"
    else:
        # sudoClear()
        print("Такого пользователя не существует!")
        return "BREAK"
    file = open(path, "r" )
    password_ = file.readline()
    file.close()
    return password_

def signIn(name = None, password = None):
    if not name:
        name = input("Введите имя пользователя: ").lower()
        password_ = input("Введите пароль: ")
    else:
        password_ = input("Повторите пароль: ")
    if not password:
        password = getPass(name)
        if password == "BREAK":
            return signIn()
    if password_ == decode(password):
        print("Вы успешно вошли в аккаунт!")
        return (name, password)
    else:
        # sudoClear()
        print("Неверный пароль!")
        return signIn(name)

def signUp():
    name = input("Придумайте имя пользователя: ").lower()
    directory = "C:\\Users\\Admin\\Desktop\\ParticleSystem2\\Accounts\\" + name
    if not os.path.exists(directory):
        os.makedirs(directory)
        file = open(directory + "\\pass.txt", "w")
        password = input("Придумайте пароль: ")
        file.write(encode(password))

        firstParticle = {
            "particles": [
                {
                    "name": "Your First Particle!",
                    "size": 10,
                    "lifespan": 10,
                    "color": (255,255,255),
                    "shape": "cir"
                }
            ]
        }

        newJson = directory + "\\presets.json"

        _ = open(newJson, "w")
        _.close()

        with open(newJson, "w") as presets:
            json.dump(firstParticle,presets)

        file.close()
        return signIn(name, password)
    else:
        print("Пользователь с таким именем уже существует!")
        return signUp()


def launch():
    ans = input("В первый раз? [Y/N]\n").upper()
    if ans == "Y":
        print("РЕГИСТРАЦИЯ")
        return signUp()
    elif ans == "N":
        return signIn()
    else:
        print("ERROR: WRONG ANSWER")
