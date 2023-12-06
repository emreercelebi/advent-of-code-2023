from readFile import read_file

lines = read_file("inputs/day3.txt")

directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

def extract_num(lines, row, col):
    c = col
    num = 0
    is_part = False
    while c < len(lines[row]) and lines[row][c].isdigit():
        num = num * 10 + int(lines[row][c])
        for dir in directions:
            new_row = row + dir[0]
            new_col = c + dir[1]
            in_bounds = new_row >= 0 and new_row < len(lines) and new_col >= 0 and new_col < len(lines[0])
            if in_bounds and not (lines[new_row][new_col].isdigit() or lines[new_row][new_col] == '.'):
                is_part = True
        c += 1
    return num, is_part, c - col

def extract_num_and_add_to_gear_map(lines, gear_map, row, col):
    gears = set()
    c = col
    num = 0
    while c < len(lines[row]) and lines[row][c].isdigit():
        num = num * 10 + int(lines[row][c])
        for dir in directions:
            new_row = row + dir[0]
            new_col = c + dir[1]
            in_bounds = new_row >= 0 and new_row < len(lines) and new_col >= 0 and new_col < len(lines[0])
            if in_bounds and not (lines[new_row][new_col].isdigit() or lines[new_row][new_col] == '.'):
                if lines[new_row][new_col] == '*':
                    gears.add((new_row, new_col))
        c += 1
    
    for gear in gears:
        if gear not in gear_map:
            gear_map[gear] = []
        gear_map[gear].append(num)
    
    return c - col

def part1():
    part_num_sum = 0
    row = 0
    while row < len(lines):
        col = 0
        while col < len(lines[row]):
            if lines[row][col].isdigit():
                num, is_part, length = extract_num(lines, row, col)
                col += length
                if is_part:
                    part_num_sum += num
            else:
                col += 1
        row += 1
    return part_num_sum

def part2():
    gear_map = {}
    gear_ratio_sum = 0
    row = 0
    while row < len(lines):
        col = 0
        while col < len(lines[row]):
            if lines[row][col].isdigit():
                length = extract_num_and_add_to_gear_map(lines, gear_map, row, col)
                col += length
            else:
                col += 1
        row += 1
    
    for gear in gear_map:
        if len(gear_map[gear]) == 2:
            gear_ratio_sum += gear_map[gear][0] * gear_map[gear][1]

    return gear_ratio_sum

print("part 1: ", part1())
print("part 2: ", part2())