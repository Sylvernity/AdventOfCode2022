f = open("AoC1Input", "r")
resolve = {"A": "Rock", "B":"Paper", "C": "Scissors", "X": "Lose", "Y": "Draw", "Z": "Win"}
count = 0
for line in f:
    sep = line.split(" ")
    sep[1] = sep[1][:1]
    one = resolve[sep[0]]
    two = resolve[sep[1]]
    if two == "Lose":
        if one == "Rock":
            count += 3
        elif one == "Paper":
            count += 1
        else:
            count += 2
    elif two == "Draw":
        count += 3
        if one == "Rock":
            count += 1
        elif one == "Paper":
            count += 2
        else:
            count += 3
    else:
        count += 6
        if one == "Rock":
            count += 2
        elif one == "Paper":
            count += 3
        else:
            count += 1
print(count)