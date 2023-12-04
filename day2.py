from readFile import read_file

lines = read_file("inputs/day2.txt")

num_red_cubes = 12
num_green_cubes = 13
num_blue_cubes = 14

def is_game_possible(line: str):
    rounds = line.split(":")[1].split(";")
    for game_round in rounds:
        game_round = game_round.strip()
        cube_groups = game_round.split(",")
        for cube_group in cube_groups:
            parts = cube_group.strip().split(" ")
            count = int(parts[0])
            color = parts[1]
            if ((color == 'red' and count > num_red_cubes) or 
            (color == 'green' and count > num_green_cubes) or 
            (color == 'blue' and count > num_blue_cubes)):
                return False 
            
    return True

def get_power(line: str):
    max_red = 0
    max_green = 0
    max_blue = 0
    rounds = line.split(":")[1].split(";")
    for game_round in rounds:
        game_round = game_round.strip()
        cube_groups = game_round.split(",")
        for cube_group in cube_groups:
            parts = cube_group.strip().split(" ")
            count = int(parts[0])
            color = parts[1]
            if color == 'red':
                max_red = max(max_red, count)
            if color == 'green':
                max_green = max(max_green, count)
            if color == 'blue':
                max_blue = max(max_blue, count)
            
    power = 1
    if max_red > 0:
        power *= max_red
    if max_green > 0:
        power *= max_green
    if max_blue > 0:
        power *= max_blue

    return power

def part1():
    result = 0
    for i in range(len(lines)):
        if is_game_possible(lines[i]):
            result += i + 1

    return result

def part2():
    result = 0
    for line in lines:
        result += get_power(line)
    return result

print("part 1: ", part1())
print("part 2: ", part2())