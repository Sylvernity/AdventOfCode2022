f = open("AoC1Input", "r")
sum = 0
list = []

for line in f:
    try:
        sum += int(line)
    except:
        list.append(sum)
        sum = 0
print(list)
print(max(list))
