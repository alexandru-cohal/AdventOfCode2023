def findReflection(numbers):
    for idx, elem in enumerate(numbers[:-1]):
        if numbers[idx] == numbers[idx + 1]:
            leftLim = 0
            rightLim = (idx + 1) * 2 - 1
            if rightLim > len(numbers) - 1:
                leftLim += (rightLim + 1) - len(numbers)
                rightLim = len(numbers) - 1
            if numbers[leftLim:idx] == numbers[rightLim:idx+1:-1]:
                return idx
    return -1

def part1(file):
    total = 0

    map = []
    for line in file:
        if line != '\n':
            map.append(line[:-1])
        else:
            numLines = len(map)
            numCols = len(map[0])

            lineNumbers = [0] * numLines
            colNumbers = [0] * numCols
            for idxLine, line in enumerate(map):
                for idxCol, elem in enumerate(line):
                    if elem == '#':
                        lineNumbers[idxLine] += pow(2, idxCol)
                        colNumbers[idxCol] += pow(2, idxLine)
            map = []

            horizReflection = findReflection(lineNumbers)
            if horizReflection != -1:
                total += 100 * (horizReflection + 1)
            else:
                vertReflection = findReflection(colNumbers)
                if vertReflection != -1:
                    total += vertReflection + 1

    return total

if __name__ == '__main__':
    file = open("inputs/day13.txt", "r")
    print(part1(file))
