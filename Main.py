import importlib
import importlib.util
import os
import time

def prettyModeRun(dayCount):
    for day in range(dayCount):
        print(f'Day {day}\t')

def runDay(day, skipPrints=False, useExampleData=False):
    # Import code for day
    # daySpec = importlib.util.spec_from_file_location(module_name, file_path)
    dayModule = importlib.import_module(f'Day{day}', package=None)

    # Figure out if using example data or real data
    useRealData = not useExampleData
    if not skipPrints:
        userInput = input("Example or Real Input? (E/r):")
        useRealData = userInput == 'r'

    # Read in the input and run day
    with open(f'{"Input" if useRealData else "ExampleInput"}/{day}.txt', 'r') as inputFile:
        fileData = inputFile.read()
        start = time.time()
        part1Output = dayModule.part1(fileData)
        endPart1 = time.time()
        part2Output = dayModule.part2(fileData)
        endPart2 = time.time()
        if not skipPrints:
            print(f'Part 1 ({endPart1 - start}): {part1Output}')
            print(f'Part 2 ({endPart2 - endPart1}): {part2Output}')

        return part1Output, part2Output, endPart1 - start, endPart2 - endPart1

dirPath = "ExampleInput"
fileCount = len([file for file in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, file))])

prettyMode = False
if prettyMode:
    prettyModeRun(fileCount)
else:
    runDay(fileCount)