import re

def getMinimumLocation(seedList, mapList):
    locationList = []
    for source in seedList:
        for map in mapList:
            for interval in map:
                if source >= interval[1] and source <= interval[1] + interval[2] - 1:
                    source += interval[0] - interval[1]
                    break
        locationList.append(source)

    return min(locationList)

def part1(file):
    #Reading
    seedList = []
    mapList = []
    idxMapList = -1

    for line in file:
        readNumberList = re.findall("\d+", line)

        if not seedList:
            seedList = [int(number) for number in readNumberList]
        elif line != '\n' and not readNumberList:
            idxMapList += 1
            mapList.append([])
        elif readNumberList:
            range = [int(number) for number in readNumberList]
            mapList[idxMapList].append(range)

    #Solving
    return getMinimumLocation(seedList, mapList)

def part2(file):
    #Reading
    seedList = []
    mapList = []
    idxMapList = -1

    for line in file:
        readNumberList = re.findall("\d+", line)

        if not seedList:
            readSeedList = [int(number) for number in readNumberList]
            for idxReadSeedList in range(0, len(readSeedList), 2):
                seedList = seedList + list(range(readSeedList[idxReadSeedList],
                                                 readSeedList[idxReadSeedList] + readSeedList[idxReadSeedList + 1]))
            print(len(seedList))
        elif line != '\n' and not readNumberList:
            idxMapList += 1
            mapList.append([])
        elif readNumberList:
            interval = [int(number) for number in readNumberList]
            mapList[idxMapList].append(interval)

    #Solving
    return getMinimumLocation(seedList, mapList)

if __name__ == '__main__':
    file = open("inputs/day5.txt", "r")
    print(part1(file))

    #file.seek(0)
    #print(part2(file))
