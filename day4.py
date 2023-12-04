import re

NUM_WINNING_NUMBERS = 10
NUM_HAVING_NUMBERS = 25
NUM_CARDS = 208

def part1(file):
    sumPoints = 0

    for line in file:
        allNumberList = re.findall("\d+", line)
        winningNumbersList = allNumberList[1 : NUM_WINNING_NUMBERS+1]
        havingNumbersList = allNumberList[NUM_WINNING_NUMBERS+1 : ]
        realNumWinningNumbers = len(set(winningNumbersList).intersection(havingNumbersList))
        if realNumWinningNumbers > 0:
            sumPoints += pow(2, realNumWinningNumbers - 1)

    return sumPoints

def part2(file):
    currentCardId = -1
    copiesCard = [1] * NUM_CARDS

    for line in file:
        currentCardId += 1

        allNumberList = re.findall("\d+", line)
        winningNumbersList = allNumberList[1 : NUM_WINNING_NUMBERS+1]
        havingNumbersList = allNumberList[NUM_WINNING_NUMBERS+1 : ]
        realNumWinningNumbers = len(set(winningNumbersList).intersection(havingNumbersList))

        for iterCardId in range(currentCardId + 1, currentCardId + 1 + realNumWinningNumbers):
            copiesCard[iterCardId] += copiesCard[currentCardId]

    return sum(copiesCard)

if __name__ == '__main__':
    file = open("inputs/day4.txt", "r")
    print(part1(file))

    file.seek(0)
    print(part2(file))
