import re

def getSumPartNumbers(line):
    sumPartNumber = 0
    value = 0
    isPartNumber = False

    for idxCol, elemCurrent in enumerate(line[1]):
        if elemCurrent.isdigit():
            value = value * 10 + int(elemCurrent)
            if not isPartNumber:
                for idxLine in [0, 1, 2]:
                    for idxColOffset in [-1, 0, 1]:
                        elemNeighb = line[idxLine][idxCol + idxColOffset]
                        if (not elemNeighb.isdigit() and elemNeighb != '.'):
                            isPartNumber = True
        else:
            if isPartNumber:
                sumPartNumber += value
            value = 0
            isPartNumber = False

    return sumPartNumber

def part1(file):
    line = ['', '', '']
    sumPartNumber = 0

    for lineRead in file:
        lineRead = '.' + lineRead[:-1] + '.'
        line = [line[1], line[2], lineRead]

        if line[1]:
            if not line[0]:
                line[0] = '.' * len(line[1])

            sumPartNumber += getSumPartNumbers(line)

    line = [line[1], line[2], '.' * len(line[1])]
    sumPartNumber += getSumPartNumbers(line)

    return sumPartNumber

if __name__ == '__main__':
    file = open("inputs/day3.txt", "r")
    print(part1(file))
