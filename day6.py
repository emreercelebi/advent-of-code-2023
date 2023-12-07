import math
from readFile import read_file


lines = read_file("inputs/day6.txt")

times = [int(e) for e in lines[0][9:].strip().split()]
distances = [int(e) for e in lines[1][9:].strip().split()]

def part1():
    times = [int(e) for e in lines[0][9:].strip().split()]
    distances = [int(e) for e in lines[1][9:].strip().split()]
    result = 1
    for i in range(len(times)):
        t = times[i]
        d = distances[i]

        lower_bound = math.ceil((t - math.sqrt(t*t - 4*d)) / 2)
        upper_bound = math.floor((t + math.sqrt(t*t - 4*d)) / 2)
        if lower_bound*lower_bound - t * lower_bound + d == 0:
            result *= upper_bound - lower_bound - 1
        else:
            result *= upper_bound - lower_bound + 1
    return result

def part2():
    t = int("".join([e for e in lines[0][9:].strip().split()]))
    d = int("".join([e for e in lines[1][9:].strip().split()]))

    lower_bound = math.ceil((t - math.sqrt(t*t - 4*d)) / 2)
    upper_bound = math.floor((t + math.sqrt(t*t - 4*d)) / 2)
    if lower_bound*lower_bound - t * lower_bound + d == 0:
        return upper_bound - lower_bound - 1
    else:
        return upper_bound - lower_bound + 1
    

print("part 1:", part1())
print("part 2:", part2())
        