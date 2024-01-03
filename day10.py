import copy

def readPart1And2(file):
    sketch = []
    for line in file:
        sketch.append(list(line[:-1]))
        if 'S' in line:
            posS = (len(sketch) - 1, line.index('S'))

    return sketch, posS

def findAndReplaceS(sketch, posS):
    numLines = len(sketch)
    numCols = len(sketch[0])

    connectedNeighPosS = [0, 0, 0, 0] # N, E, S, W

    if posS[0] > 0 and sketch[posS[0] - 1][posS[1]] in ['|', '7', 'F']:
        connectedNeighPosS[0] = 1
    if posS[0] < numLines - 1 and sketch[posS[0] + 1][posS[1]] in ['|', 'L', 'J']:
        connectedNeighPosS[2] = 1
    if posS[1] > 0 and sketch[posS[0]][posS[1] - 1] in ['-', 'L', 'F']:
        connectedNeighPosS[3] = 1
    if posS[1] < numCols - 1 and sketch[posS[0]][posS[1] + 1] in ['-', 'J', '7']:
        connectedNeighPosS[1] = 1

    match connectedNeighPosS:
        case [1, 1, 0, 0]:
            typeS = 'L'
        case [0, 1, 1, 0]:
            typeS = 'F'
        case [0, 0, 1, 1]:
            typeS = '7'
        case [1, 0, 0, 1]:
            typeS = 'J'
        case [1, 0, 1, 0]:
            typeS = '|'
        case [0, 1, 0, 1]:
            typeS = '-'

    sketch[posS[0]][posS[1]] = typeS

    return sketch

def part1(sketch, posS):
    # Solving
    queue = [[posS[0], posS[1], 0]] # line, col, distance from S
    maxDist = 0
    while queue:
        currQueueElem = queue.pop(0)
        if isinstance(sketch[currQueueElem[0]][currQueueElem[1]], str):
            # North connection
            if sketch[currQueueElem[0]][currQueueElem[1]] in ['|', 'L', 'J']:
                if isinstance(sketch[currQueueElem[0] - 1][currQueueElem[1]], str):
                    queue.append([currQueueElem[0] - 1, currQueueElem[1], currQueueElem[2] + 1])
            # East connection
            if sketch[currQueueElem[0]][currQueueElem[1]] in ['-', 'L', 'F']:
                if isinstance(sketch[currQueueElem[0]][currQueueElem[1] + 1], str):
                    queue.append([currQueueElem[0], currQueueElem[1] + 1, currQueueElem[2] + 1])
            # South connection
            if sketch[currQueueElem[0]][currQueueElem[1]] in ['|', '7', 'F']:
                if isinstance(sketch[currQueueElem[0] + 1][currQueueElem[1]], str):
                    queue.append([currQueueElem[0] + 1, currQueueElem[1], currQueueElem[2] + 1])
            # West connection
            if sketch[currQueueElem[0]][currQueueElem[1]] in ['-', '7', 'J']:
                if isinstance(sketch[currQueueElem[0]][currQueueElem[1] - 1], str):
                    queue.append([currQueueElem[0], currQueueElem[1] - 1, currQueueElem[2] + 1])
            sketch[currQueueElem[0]][currQueueElem[1]] = currQueueElem[2]
            maxDist = max(maxDist, currQueueElem[2])

    return maxDist

def part2(sketch, sketchProcessed):
    countInLoop = 0

    for idxLine in range(len(sketch)):
        countVertBar = 0
        isLBefore = False
        countL7 = 0
        isFBefore = False
        countFJ = 0

        for idxCol in range(len(sketch[idxLine])):
            if not isinstance(sketchProcessed[idxLine][idxCol], str):
                match sketch[idxLine][idxCol]:
                    case '|':
                        countVertBar += 1
                    case 'L':
                        isLBefore = True
                    case '7':
                        if isLBefore:
                            isLBefore = False
                            countL7 += 1
                        elif isFBefore:
                            isFBefore = False
                    case 'F':
                        isFBefore = True
                    case 'J':
                        if isFBefore:
                            isFBefore = False
                            countFJ += 1
                        elif isLBefore:
                            isLBefore = False
            if isinstance(sketchProcessed[idxLine][idxCol], str):
                if (countVertBar + countL7 + countFJ) % 2 == 1:
                    countInLoop += 1

    return countInLoop

if __name__ == '__main__':
    file = open("inputs/day10.txt", "r")
    sketch, posS = readPart1And2(file)
    findAndReplaceS(sketch, posS)
    sketchOriginal = copy.deepcopy(sketch)

    print(part1(sketch, posS))

    print(part2(sketchOriginal, sketch))
