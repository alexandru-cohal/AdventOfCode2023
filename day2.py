import re

redSetCount = 12
greenSetCount = 13
blueSetCount = 14

def part1(file):
    sumGameId = 0
    for line in file:
        numberList = re.findall("\d+", line)
        colorList = re.findall("(blue|green|red)", line)
        redCount = (max([int(numberList[idx + 1]) for idx, color in enumerate(colorList) if color == 'red']))
        greenCount = (max([int(numberList[idx + 1]) for idx, color in enumerate(colorList) if color == 'green']))
        blueCount = (max([int(numberList[idx + 1]) for idx, color in enumerate(colorList) if color == 'blue']))
        if (redCount <= redSetCount) and (greenCount <= greenSetCount) and (blueCount <= blueSetCount):
            sumGameId += int(numberList[0])
    return sumGameId

def part2(file):
    sumPower = 0
    for line in file:
        numberList = re.findall("\d+", line)
        colorList = re.findall("(blue|green|red)", line)
        redCount = (max([int(numberList[idx + 1]) for idx, color in enumerate(colorList) if color == 'red']))
        greenCount = (max([int(numberList[idx + 1]) for idx, color in enumerate(colorList) if color == 'green']))
        blueCount = (max([int(numberList[idx + 1]) for idx, color in enumerate(colorList) if color == 'blue']))
        sumPower += redCount * greenCount * blueCount
    return sumPower

if __name__ == '__main__':
    file = open("inputs/day2.txt", "r")
    print(part1(file))

    file.seek(0)
    print(part2(file))
