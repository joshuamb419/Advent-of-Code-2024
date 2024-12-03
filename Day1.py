def part1(input):
    lines = input.split("\n")
    list1 = []
    list2 = []
    for line in lines:
        parts = line.split("   ")
        list1.append(int(parts[0]))
        list2.append(int(parts[1]))

    list1.sort()
    list2.sort()
    distance = 0
    for i in range(len(list1)):
        distance += abs(list1[i] - list2[i])

    return distance

def part2(input):
    lines = input.split("\n")
    list1 = []
    list2 = []
    for line in lines:
        parts = line.split("   ")
        list1.append(int(parts[0]))
        list2.append(int(parts[1]))

    score = 0
    dict = {}
    for item in list1:
        if item not in dict:
            dict[item] = item * list2.count(item)

        score += dict[item]

    return score