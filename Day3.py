def part1(input):
    i = 0
    validChars = ['m', 'u', 'l', '(', ')', ',', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    total = 0
    while i < len(input):
        if input[i] != 'm':
            i += 1
            continue

        start = i
        end = 0
        while input[i] in validChars:
            if input[i] == ')':
                end = i
                break
            i += 1

        if end == 0:
            continue
        total += performOp(input[start:end+1])
        i += 1

    return total

def performOp(str):
    if str[0:4] != "mul(" or 'd' in str or 'o' in str or 'n' in str or "'" in str or 't' in str:
        return 0
    nums = str.split("(")[1]
    num1 = int(nums.split(",")[0])
    num2 = int(nums.split(",")[1][:-1])
    return num1 * num2

def part2(input):
    i = 0
    validMul = ['m', 'u', 'l', '(', ')', ',', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'd', 'o', 'n', "'", 't']
    doStr = 'do()'
    dontStr = "don't()"
    do = True
    total = 0
    while i < len(input):
        if input[i] != 'm' and input[i] != 'd':
            i += 1
            continue
        start = i
        end = 0
        while input[i] in validMul :
            if input[i] == ')':
                end = i
                break
            i += 1

        if end == 0:
            continue

        slice = input[start:end + 1]
        if slice == doStr:
            do = True
        elif slice == dontStr:
            do = False
        else:
            if do:
                total += performOp(slice)
        i += 1

    return total