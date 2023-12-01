import re

digitsDict = {'one':    1,
              'two':    2,
              'three':  3,
              'four':   4,
              'five':   5,
              'six':    6,
              'seven':  7,
              'eight':  8,
              'nine':   9}

def digitListElemToIntPart1(digitListElem):
    return int(digitListElem) - int('0')

def digitListElemToIntPart2(digitListElem):
    if digitListElem in digitsDict:
        return digitsDict[digitListElem]
    else:
        return int(digitListElem) - int('0')

def part1(file):
    sum = 0
    for line in file:
        digits = re.findall("[0-9]", line)
        sum += digitListElemToIntPart1(digits[0]) * 10 + digitListElemToIntPart1(digits[-1])
    return sum

def part2(file):
    sum = 0
    for line in file:
        digits = re.findall("(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))", line)
        sum += digitListElemToIntPart2(digits[0]) * 10 + digitListElemToIntPart2(digits[-1])
    return sum

if __name__ == '__main__':
    file = open("inputs/day1.txt", "r")
    print(part1(file))

    file.seek(0)
    print(part2(file))
