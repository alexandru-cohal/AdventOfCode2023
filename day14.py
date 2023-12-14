def part1(file):
    map = []
    for line in file:
        map.append(line[:-1])
    numLines = len(map)
    numCols = len(map[0])
    rowLimitSliding = [0] * numCols

    totalLoad = 0
    for idxLine, line in enumerate(map):
        for idxCol, elem in enumerate(line):
            if elem == '#':
                rowLimitSliding[idxCol] = idxLine + 1
            elif elem == 'O':
                totalLoad += numLines - rowLimitSliding[idxCol]
                rowLimitSliding[idxCol] += 1

    return totalLoad

if __name__ == '__main__':
    file = open("inputs/day14.txt", "r")
    print(part1(file))
