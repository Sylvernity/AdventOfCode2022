f = open("AoC1Input", "r")
sum = 0
list = []

for line in f:
    try:
        sum += int(line)
    except:
        list.append(sum)
        sum = 0

oneMost = max(list)
list.remove(oneMost)

twoMost = max(list)
list.remove(twoMost)

threeMost = max(list)

sum = oneMost + twoMost + threeMost
print(sum)