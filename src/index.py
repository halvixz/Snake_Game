from Map import *
from Snake import *
import keyboard as kd

def main():
    direction = (0, 1)
    while 1:

        if kd.is_pressed('w') and odd != (1, 0):
            direction = (-1, 0)
        elif kd.is_pressed('s') and odd != (-1, 0):
            direction = (1, 0)
        elif kd.is_pressed('d') and odd != (0, -1):
            direction = (0, 1)
        elif kd.is_pressed('a') and odd != (0, 1):
            direction = (0, -1)
            
        move(direction, map)
        draw(body)
        display()

if (__name__ == "__main__"):
    main()