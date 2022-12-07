f = open("AoCInput", "r")
count = 0
elves = [x.strip() for x in f]


for line in elves:
    line.strip("\n")
    print(line)
    both = line.split(",")
    print(both)
    one = both[0].split("-")
    one = [int(x) for x in one]
    two = both[1].split("-")
    two = [int(x) for x in two]
    print(one)
    print(two)

    if ((one[0] <= two[0]) and (one[1] >= two[1])) or ((two[0] <= one[0]) and (two[1] >= one[1])):
        count += 1
    print(count)
print(count)