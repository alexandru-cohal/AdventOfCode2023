import re

def getCardValue(card):
    match card:
        case 'A':
            return 14
        case 'K':
            return 13
        case 'Q':
            return 12
        case 'J':
            return 11
        case 'T':
            return 10
        case _:
            return int(card)

def funcSortHandsByType(hand):
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

def funcSortHandsByValue(hand):
    value = 0
    for card in hand[0]:
        value = value * 15 + getCardValue(card)
    return value

def part1(file):
    handList = []
    for line in file:
        handList.append(re.findall("\w+", line))

    handList.sort(reverse=True, key=funcSortHandsByValue)
    handList.sort(reverse=True, key=funcSortHandsByType)

    totalWining = 0
    for idxHand, hand in enumerate(handList):
        totalWining += (len(handList) - idxHand) * int(hand[1])

    return totalWining

if __name__ == '__main__':
    file = open("inputs/day7.txt", "r")
    print(part1(file))
