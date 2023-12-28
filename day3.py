import re

def readPart1And2(file):
    # Reading
    numberList = []
    symbolList = []
    number = 0
    posStart = posEnd = None
    lineIndex = -1

    for line in file:
        lineIndex += 1
        numberList.append([])
        symbolList.append([])
        for elemIndex, elem in enumerate(line):
            if '0' <= elem <= '9':
                number = number * 10 + int(elem)
                if posStart is None:
                    posStart = elemIndex
                posEnd = elemIndex
            else:
                if number:
                    numberList[lineIndex].append([number, posStart, posEnd])
                    posStart = posEnd = None
                    number = 0
                if elem not in ['\n', '.']:
                    symbolList[lineIndex].append([elem, elemIndex])

    return numberList, symbolList

def isPartNumber(line, colStart, colEnd, symbolList):
    for lineIndex in range(max(0, line-1), min(len(symbolList)-1, line+1) + 1):
        for symbol in symbolList[lineIndex]:
            # symbol = symbol[0], pos = symbol[1]
            if colStart - 1 <= symbol[1] <= colEnd + 1:
                return True
    return False

def part1(numberList, symbolList):
    sumPartNumber = 0

    for lineNumberIndex, lineNumber in enumerate(numberList):
        for number in lineNumber:
            # value = number[0], posStart = number[1], posEnd = number[2]
            if isPartNumber(lineNumberIndex, number[1], number[2], symbolList):
                sumPartNumber += number[0]
    return sumPartNumber

def isGear(line, col, numberList):
    numAdjPartNumber = 0
    gearRatio = 1

    for lineIndex in range(max(0, line-1), min(len(numberList)-1, line+1) + 1):
        for number in numberList[lineIndex]:
            # value = number[0], posStart = number[1], posEnd = number[2]
            if number[1] - 1 <= col <= number[2] + 1:
                numAdjPartNumber += 1
                gearRatio *= number[0]

    if numAdjPartNumber == 2:
        return gearRatio
    else:
        return None

def part2(numberList, symbolList):
    sumGearRatio = 0

    for lineSymbolIndex, lineSymbol in enumerate(symbolList):
        for symbol in lineSymbol:
            # symbol = symbol[0], pos = symbol[1]
            if symbol[0] == '*':
                gearRatio = isGear(lineSymbolIndex, symbol[1], numberList)
                if gearRatio:
                    sumGearRatio += gearRatio

    return sumGearRatio

if __name__ == '__main__':
    file = open("inputs/day3.txt", "r")
    numberList, symbolList = readPart1And2(file)

    print(part1(numberList, symbolList))

    print(part2(numberList, symbolList))
