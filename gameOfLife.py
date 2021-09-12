# Conway's Game of Life
import random, time, copy
WIDTH = 4
HEIGHT = 4

nextCells = []
for x in range(WIDTH):
    columns = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            columns.append('o') #Alive
        else:
            columns.append('x') #Dead
    nextCells.append(columns)

while True:
    print('\n\n\n\n')
    currentCells = copy.deepcopy(nextCells)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end="")
        print()

    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == 'o':
                numNeighbors += 1
            if currentCells[leftCoord][y] == 'o':
                numNeighbors += 1
            if currentCells[leftCoord][belowCoord] == 'o':
                numNeighbors += 1
            if currentCells[x][aboveCoord] == 'o':
                numNeighbors += 1
            if currentCells[x][belowCoord] == 'o':
                numNeighbors += 1
            if currentCells[rightCoord][aboveCoord] == 'o':
                numNeighbors += 1
            if currentCells[rightCoord][y] == 'o':
                numNeighbors += 1
            if currentCells[rightCoord][belowCoord] == 'o':
                numNeighbors += 1
            if currentCells[x][y] == 'o' and (numNeighbors == 2 or numNeighbors == 3):
                nextCells[x][y] = 'o'
            elif currentCells[x][y] == 'x' and numNeighbors == 3:
                nextCells[x][y] = 'o'
            else:
                nextCells[x][y] = 'x'
    time.sleep(5)
