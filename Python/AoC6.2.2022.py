f = open("AoCInput", "r")

markerIndex = 0
string = f.read()
for startIndex in range(0, len(string) - 14):
    endIndex = startIndex + 14
    sequence = string[startIndex: endIndex]
    print(sequence)
    letterIndex = 0
    while letterIndex < 14:
        letter = sequence[letterIndex]
        try:
            firstIndex = sequence.index(letter)
            secondIndex = sequence[firstIndex + 1:].index(letter)
            letterIndex = 20
        except:
            letterIndex += 1
    if letterIndex != 20:
        print(endIndex)
        break
