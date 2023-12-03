from readFile import read_file

lines = read_file("inputs/day1.txt")
numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

def get_calibration_number(line):
    calibration_number = 0
    for i in range(len(line)):
        if line[i].isdigit():
            calibration_number += int(line[i]) * 10
            break
        
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            calibration_number += int(line[i])
            break
        
    return calibration_number

def get_calibration_number2(line):
    calibration_number = 0
    for i in range(len(line)):
        if line[i].isdigit():
            calibration_number += int(line[i]) * 10
            break
        else:
            num_found = False
            for j in range(3, 6):
                if line[i:i + j] in numbers:
                    num_found = True
                    calibration_number += int(numbers[line[i:i + j]]) * 10
                    break
            if num_found:
                break
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            calibration_number += int(line[i])
            break
        else:
            num_found = False
            for j in range(3, 6):
               if line[i:i + j] in numbers:
                    num_found = True
                    calibration_number += int(numbers[line[i:i + j]]) 
                    break
            if num_found:
                break
            
    return calibration_number
        

def part1():
    calibration_number_total = 0
    for line in lines:
        calibration_number_total += get_calibration_number(line)
    return calibration_number_total

def part2():
    calibration_number_total = 0
    for line in lines:
        calibration_number_total += get_calibration_number2(line)
    return calibration_number_total

print("part 1: ", part1())
print("part 2: ", part2())
    