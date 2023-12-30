import re

def readPart1And2(file):
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

    return seedList, mapList

def part1(seedList, mapList):
    locationList = []
    for source in seedList:
        for map in mapList:
            for interval in map:
                if source >= interval[1] and source <= interval[1] + interval[2] - 1:
                    source += interval[0] - interval[1]
                    break
        locationList.append(source)

    return min(locationList)

def part2(seedList, mapList):
    # Prepare initial intervals
    currIntervalList = []
    itSeedList = iter(seedList)
    for seedListElem in itSeedList:
        currIntervalList.append([seedListElem, seedListElem + next(itSeedList) - 1])

    # Apply mappings
    for map in mapList:
        newIntervalList = []
        idxCurrInterv = 0
        while idxCurrInterv < len(currIntervalList):
            currInterv = currIntervalList[idxCurrInterv]
            # minValDestMapInterv = mapInterval[0], minValSrcMapInter = mapInterval[1], lengthMapInterv = mapInterval[2]
            for mapInterval in map:
                # minValueCurrentInterval = currentInterval[0], maxValueCurrentInterval = currentInterval[1]
                minCurrInterv = currInterv[0]
                maxCurrInterv = currInterv[1]
                minMapSrcInterv = mapInterval[1]
                maxMapSrcInterv = mapInterval[1] + mapInterval[2] - 1
                offsetMap = mapInterval[0] - mapInterval[1]
                if (minMapSrcInterv <= minCurrInterv <= maxMapSrcInterv) or (minMapSrcInterv <= maxCurrInterv <= maxMapSrcInterv):
                    # Overlap of intervals
                    if (minMapSrcInterv <= minCurrInterv <= maxMapSrcInterv) and (maxMapSrcInterv < maxCurrInterv):
                        # Overlap of left side of currentInterval
                        newIntervalList.append([minCurrInterv + offsetMap, maxMapSrcInterv + offsetMap])
                        currIntervalList[idxCurrInterv] = [maxMapSrcInterv + 1, maxCurrInterv]
                        currInterv = currIntervalList[idxCurrInterv]
                    elif (minMapSrcInterv <= maxCurrInterv <= maxMapSrcInterv) and (minCurrInterv < minMapSrcInterv):
                        # Overlap of right side of currentInterval
                        currIntervalList[idxCurrInterv] = [minCurrInterv, minMapSrcInterv - 1]
                        currInterv = currIntervalList[idxCurrInterv]
                        newIntervalList.append([minMapSrcInterv + offsetMap, maxCurrInterv + offsetMap])
                    else:
                        # Overlap of whole currentInterval
                        newIntervalList.append([minCurrInterv + offsetMap, maxCurrInterv + offsetMap])
                        currIntervalList.pop(idxCurrInterv)
                        idxCurrInterv -= 1
                        break
            idxCurrInterv += 1
        currIntervalList += newIntervalList

    # Find the lowest value from currIntervalList
    minValCurrInterv = currIntervalList[0][0]
    for currInterv in currIntervalList:
        minValCurrInterv = min(minValCurrInterv, currInterv[0])

    return minValCurrInterv

if __name__ == '__main__':
    file = open("inputs/day5.txt", "r")
    seedList, mapList = readPart1And2(file)

    print(part1(seedList, mapList))

    print(part2(seedList, mapList))
