f = open("AoC1Input", "r")
alpha = "1abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
sum = 0

elves = f.readlines()
elves = [x.strip() for x in elves]
i = 0
while i <= 299:
    one = elves[i]
    i += 1
    two = elves[i]
    i += 1
    three = elves[i]
    i += 1

    for letter in one:
        try:
            two.index(letter)
            three.index(letter)
            sum += alpha.index(letter)
            print(str(i) + letter)
            break
        except:
            j = 0
print(sum)