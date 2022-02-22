from os import system
from random import randint

map = []
score = -1
fruit = [0,0]

LINE_COUNT = 10
ITENS_PER_LINE = 11

def resetMap():
    global map
    map = []
    for i in range(LINE_COUNT):
        map.append([])
        if (i == 0 or i == LINE_COUNT-1):
            for j in range(ITENS_PER_LINE):
                map[i].append('*')
        else:
            for j in range(ITENS_PER_LINE):
                if (j == 0 or j == ITENS_PER_LINE-1):
                    map[i].append('*')
                else:
                    map[i].append(' ')

resetMap()

def display():
    global map
    system("cls")
    print(score)
    print("-"*(ITENS_PER_LINE*2-1))
    for m in map:
        print(*m)
        
def generateFruit(body):
    fruit[0] = randint(1, LINE_COUNT-2)
    fruit[1] = randint(1, ITENS_PER_LINE-2)

    while (fruit in body):
        fruit[0] = randint(1, LINE_COUNT-2)
        fruit[1] = randint(1, ITENS_PER_LINE-2)

    map[fruit[0]][fruit[1]] = '#'

def draw(snake):
    for p in snake:
        if ((p[0] >= LINE_COUNT-1 or p[0] <= 0) or (p[1] >= ITENS_PER_LINE-1 or p[1] <= 0)):
            print("Game over!")
            quit(0)
        map[p[0]][p[1]] = 'o'
    if (map[fruit[0]][fruit[1]] != '#'):
        global score
        score += 1
        generateFruit(body=snake)
        snake.append([snake[len(snake)-1][0], snake[len(snake)-1][1]])
        
