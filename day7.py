import re

def funcSortHandsByTypePart1(hand):
    cards = sorted(hand[0])
    kindCount = [0, 0, 0, 0, 0, 0] #[placeholder, 1kind, 2kind, 3kind, 4kind, 5kind]
    kindCurr = 1
    for idxCard in range(len(cards) - 1):
        if cards[idxCard] == cards[idxCard + 1]:
            kindCurr += 1
        else:
            kindCount[kindCurr] += 1
            kindCurr = 1
    kindCount[kindCurr] += 1

    if kindCount[5] == 1:
        handType = 6
    elif kindCount[4] == 1:
        handType = 5
    elif kindCount[3] == 1 and kindCount[2] == 1:
        handType = 4
    elif kindCount[3] == 1 and kindCount[2] == 0:
        handType = 3
    elif kindCount[2] == 2:
        handType = 2
    elif kindCount[2] == 1:
        handType = 1
    else:
        handType = 0

    return handType

def funcSortHandsByTypePart2(hand):
    cards = sorted(hand[0])
    kindCount = [0, 0, 0, 0, 0, 0] #[placeholder, 1kind, 2kind, 3kind, 4kind, 5kind]
    kindCurr = 1
    jCount = 0
    for idxCard in range(len(cards)):
        if cards[idxCard] == 'J':
            jCount += 1
        elif idxCard < len(cards) - 1:
            if cards[idxCard] == cards[idxCard + 1]:
                kindCurr += 1
            else:
                kindCount[kindCurr] += 1
                kindCurr = 1
        else:
            kindCount[kindCurr] += 1

    if jCount > 0:
        if kindCount[4] == 1:
            kindCount[4] = 0
            kindCount[5] = 1
        elif kindCount[3] == 1 and kindCount[2] == 0:
            kindCount[3] = 0
            kindCount[3 + jCount] = 1
        elif kindCount[2] > 0:
            kindCount[2] -= 1
            kindCount[2 + jCount] = 1
        elif kindCount[1] > 0:
            kindCount[1 + jCount] = 1
            kindCount[1] -= 1
        else:
            kindCount[5] = 1

    if kindCount[5] == 1:
        handType = 6
    elif kindCount[4] == 1:
        handType = 5
    elif kindCount[3] == 1 and kindCount[2] == 1:
        handType = 4
    elif kindCount[3] == 1 and kindCount[2] == 0:
        handType = 3
    elif kindCount[2] == 2:
        handType = 2
    elif kindCount[2] == 1:
        handType = 1
    else:
        handType = 0

    return handType

def getCardValue(card, part):
    match card:
        case 'A':
            return 14
        case 'K':
            return 13
        case 'Q':
            return 12
        case 'J':
            if part == 1:
                return 11
            else:
                return 1
        case 'T':
            return 10
        case _:
            return int(card)

def funcSortHandsByValuePart1(hand):
    value = 0
    for card in hand[0]:
        value = value * 15 + getCardValue(card, 1)
    return value

def funcSortHandsByValuePart2(hand):
    value = 0
    for card in hand[0]:
        value = value * 15 + getCardValue(card, 2)
    return value

def part1(file):
    handList = []
    for line in file:
        handList.append(re.findall("\w+", line))

    handList.sort(reverse=True, key=funcSortHandsByValuePart1)
    handList.sort(reverse=True, key=funcSortHandsByTypePart1)

    totalWining = 0
    for idxHand, hand in enumerate(handList):
        totalWining += (len(handList) - idxHand) * int(hand[1])

    return totalWining

def part2(file):
    handList = []
    for line in file:
        handList.append(re.findall("\w+", line))

    handList.sort(reverse=True, key=funcSortHandsByValuePart2)
    handList.sort(reverse=True, key=funcSortHandsByTypePart2)

    totalWining = 0
    for idxHand, hand in enumerate(handList):
        totalWining += (len(handList) - idxHand) * int(hand[1])

    return totalWining

if __name__ == '__main__':
    file = open("inputs/day7.txt", "r")
    print(part1(file))

    file.seek(0)
    print(part2(file))
