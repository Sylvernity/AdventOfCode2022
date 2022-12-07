f = open("AoC1Input", "r")
resolve = {"A": "Rock", "B":"Paper", "C": "Scissors", "X": "Rock", "Y": "Paper", "Z": "Scissors"}
shape = {"Rock": 1, "Paper":2, "Scissors":3}
p1 = 0
p2 = 0
for line in f:
    sep = line.split(" ")
    sep[1] = sep[1][:1]
    one = resolve[sep[0]]
    two = resolve[sep[1]]
    if one == two:
        p1 += 3
        p2 += 3
    elif (one == "Rock" and two == "Scissors") or (one == "Paper" and two == "Rock") or (one == "Scissors" and two == "Paper"):
        p1 += 6
    else:
        p2 += 6
    p1 += shape[one]
    p2 += shape[two]
print(p2)