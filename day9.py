import re

def part1(file):
    sumValuePredicted = 0

    for line in file:
        valueList = [int(value) for value in re.findall("-*\d+", line)]
        valuePredicted = valueList[-1]
        allValuesZero = False

        while not allValuesZero:
            allValuesZero = True
            for idx in range(len(valueList) - 1):
                valueList[idx] = valueList[idx + 1] - valueList[idx]
                if valueList[idx] != 0:
                    allValuesZero = False
            valueList = valueList[:-1]
            valuePredicted += valueList[-1]

        sumValuePredicted += valuePredicted

    return sumValuePredicted

def part2(file):
    sumValuePredicted = 0

    for line in file:
        valueList = [int(value) for value in re.findall("-*\d+", line)]
        valuePredicted = valueList[0]
        signNextTerm = 1
        allValuesZero = False

        while not allValuesZero:
            signNextTerm *= -1
            allValuesZero = True
            for idx in range(len(valueList) - 1):
                valueList[idx] = valueList[idx + 1] - valueList[idx]
                if valueList[idx] != 0:
                    allValuesZero = False
            valueList = valueList[:-1]
            valuePredicted += signNextTerm * valueList[0]

        sumValuePredicted += valuePredicted

    return sumValuePredicted

if __name__ == '__main__':
    file = open("inputs/day9.txt", "r")
    print(part1(file))

    file.seek(0)
    print(part2(file))
