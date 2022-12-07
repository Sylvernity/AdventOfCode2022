dock = [['R', 'N', 'P', 'G'], ['T', 'J', 'B', 'L', 'C', 'S', 'V', 'H'], ['T', 'D', 'B', 'M', 'N', 'L'], ['R', 'V', 'P', 'S', 'B'], ['G', 'C', 'Q', 'S', 'W', 'M', 'V', 'H'], ['W', 'Q', 'S', 'C', 'D', 'B', 'J'], ['F', 'Q', 'L'], ['W', 'M', 'H', 'T', 'D', 'L', 'F', 'V'], ['L', 'P', 'B', 'V', 'M', 'J', 'F']]

f = open("AoCInput", "r")

for line in f:
    line = line.strip()
    temp = line.split()
    instruct = [int(temp[1]), int(temp[3]), int(temp[5])]
    print(instruct[0])
    switchList = []
    endPileNumber = instruct[2] - 1

    for i in range(0, instruct[0]):
        startPileNumber = instruct[1] - 1
        endPileNumber = instruct[2] - 1
        startPile = dock[startPileNumber]
        letter = startPile[len(startPile) - 1]

        dock[startPileNumber] = dock[startPileNumber][:len(startPile) - 1]
        switchList.append(letter)

    switchList.reverse()
    dock[endPileNumber].extend(switchList)
    print(dock[endPileNumber])

for i in dock:
    print(i[len(i) - 1])