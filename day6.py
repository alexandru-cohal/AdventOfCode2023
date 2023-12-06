import re
from math import sqrt, floor, ceil

def getNumberWinningWays(time, dist):
    sqrtTerm = sqrt(pow(time, 2) - 4 * dist)

    limitLeft = (time - sqrtTerm) / 2
    if limitLeft.is_integer():
        limitLeft = int(limitLeft + 1)
    else:
        limitLeft = ceil(limitLeft)

    limitRight = (time + sqrtTerm) / 2
    if limitRight.is_integer():
        limitRight = int(limitRight - 1)
    else:
        limitRight = floor(limitRight)

    return (limitRight - limitLeft + 1)

def part1(file):
    timeList = [int(elem) for elem in re.findall("\d+", file.readline())]
    distList = [int(elem) for elem in re.findall("\d+", file.readline())]
    marginError = 1

    for idx in range(len(timeList)):
        marginError *= getNumberWinningWays(timeList[idx], distList[idx])

    return marginError

def part2(file):
    time = ''
    dist = ''

    timeList = re.findall("\d+", file.readline())
    for elemCurrent in timeList:
        time = time + elemCurrent
    distList = re.findall("\d+", file.readline())
    for elemCurrent in distList:
        dist = dist + elemCurrent

    return getNumberWinningWays(int(time), int(dist))


if __name__ == '__main__':
    file = open("inputs/day6.txt", "r")
    print(part1(file))

    file.seek(0)
    print(part2(file))
