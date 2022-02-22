body = [[5, 5], [5, 4], [5, 3], [5, 2]];

cdelay = 0
delay = 13

odd = []

def verifyDie():
    for b in body:
        if (body.count(b) > 1):
            print("Game over!")
            quit(0)

def move(direction, map):
    global delay, cdelay
    if cdelay >= delay:
        global odd
        odd = direction
        map[body[len(body)-1][0]][body[len(body)-1][1]] = ' '
        body.pop(len(body)-1)
        body.insert(0, [body[0][0], body[0][1]])
        body[0][0] += direction[0]
        body[0][1] += direction[1]
        verifyDie()
        cdelay = 0
    else: 
        cdelay += 1
    
