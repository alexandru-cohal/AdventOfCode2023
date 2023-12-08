import re
from math import lcm

def part1(file):
    instrucList = file.readline()[:-1]
    file.readline() #Blank line
    networkDict = {}
    for line in file:
        elemList = re.findall("[A-Z]+", line)
        networkDict[elemList[0]] = [elemList[1], elemList[2]]

    elemCurrent = 'AAA'
    stepCount = 0
    while elemCurrent != 'ZZZ':
        if instrucList[stepCount % len(instrucList)] == 'L':
            elemCurrent = networkDict[elemCurrent][0]
        else:
            elemCurrent = networkDict[elemCurrent][1]
        stepCount += 1

    return stepCount

def part2(file):
    instrucList = file.readline()[:-1]
    file.readline() #Blank line
    networkDict = {}
    for line in file:
        elemList = re.findall("[A-Z]+", line)
        networkDict[elemList[0]] = [elemList[1], elemList[2]]

    elemCurrentList = [elem for elem in networkDict if elem[2] == 'A']

    """
    Particular Solution: It was observed that for each starting element (i.e. element ending in 'A'),
    the same ending element (i.e. element ending in 'Z') will be reached after an integer multiple of 
    the total length of instruction lists and will always lead to the same ending element. This is a 
    very "happy" case of circularity. It would have been much worse if for each starting element,
    different ending elements would have been reached at different points from the instructions list.
    So, considering this "happy" case, the solution is given by the Least Common Multiplier of the
    number of steps needed for each starting element to reach for the first time their corresponding
    ending element. So, this is not a general solution, it is tailored for this specific case.
    """

    stepCountsUntilEndList = []
    for elemCurrent in elemCurrentList:
        stepCount = 0
        while elemCurrent[2] != 'Z':
            if instrucList[stepCount % len(instrucList)] == 'L':
                elemCurrent = networkDict[elemCurrent][0]
            else:
                elemCurrent = networkDict[elemCurrent][1]
            stepCount += 1
        stepCountsUntilEndList.append(stepCount)

    return lcm(*stepCountsUntilEndList)

if __name__ == '__main__':
    file = open("inputs/day8.txt", "r")
    print(part1(file))

    file.seek(0)
    print(part2(file))
