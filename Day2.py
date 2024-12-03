def part1(input):
    lines = input.split("\n")
    safeLines = 0
    for j in range(len(lines)):
        line = lines[j]
        levels = [int(item) for item in line.split(" ")]
        safe = True
        increasing = False
        for i in range(len(levels))[1:]:
            if levels[i] == levels[i-1]:
                safe = False
                break

            if i == 1 and levels[i-1] < levels[i]:
                increasing = True

            change = (levels[i] - levels[i - 1])
            if not increasing:
                change *= -1

            if change < 1 or change > 3:
                safe = False
                break

        if safe:
            safeLines += 1

    return safeLines

def checkLevels(levels, hasError=True):
    safe = True
    increasing = False
    for i in range(len(levels))[1:]:
        if levels[i] == levels[i - 1]:
            safe = False
            break

        if i == 1 and levels[i - 1] < levels[i]:
            increasing = True

        change = (levels[i] - levels[i - 1])
        if not increasing:
            change *= -1

        if change < 1 or change > 3:
            safe = False
            break

    if hasError:
        return safe

    for i in range(len(levels)):
        if checkLevels(levels[:i] + levels[i+1:]):
            return True

def part2(input):
    lines = input.split("\n")
    safeLines = 0
    for j in range(len(lines)):
        line = lines[j]
        levels = [int(item) for item in line.split(" ")]
        safe = checkLevels(levels, False)
        if safe:
            safeLines += 1

    return safeLines