import pyperclip
import random
import keyboard


def copy():
    keyboard.wait('control+c')
    chance = random.randint(0, 4)
    if chance == 0:
        pyperclip.copy('Big A')

    copy()


copy()
