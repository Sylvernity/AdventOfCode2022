f = open("AoCInput", "r")

markerIndex = 0
string = f.read()
for startIndex in range(0, len(string) - 4):
    endIndex = startIndex + 4
    sequence = string[startIndex: endIndex]
    print(sequence)
    letterIndex = 0
    while letterIndex < 4:
        letter = sequence[letterIndex]
        try:
            firstIndex = sequence.index(letter)
            secondIndex = sequence[firstIndex + 1:].index(letter)
            letterIndex = 5
        except:
            letterIndex += 1
    if letterIndex != 5:
        print(endIndex)
        break
