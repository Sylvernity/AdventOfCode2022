f = open("AoC1Input", "r")
alpha = "1abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sum = 0
i = 1
list =
for line in f:
    line = line[:len(line)-1]
    half = int(len(line) / 2)
    one = line[:half]
    two = line[half:]
    newOne = list(set(one))
    for letter in newOne:
        try:
            two.index(letter)
            sum += alpha.index(letter)
            print(str(i) + letter + ": " + line)
            i += 1
        except:
            j = 0
print(sum-alpha.index("T"))