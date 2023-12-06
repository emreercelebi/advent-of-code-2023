from readFile import read_file

lines = read_file("inputs/day5.txt")

class Mapping:
    def __init__(self, destination, source, range):
        self.destination = destination
        self.source = source
        self.range = range

    def get_value(self, source_key):
        if source_key >= (self.source + self.range) or source_key < self.source:
            return source_key
        else:
            return self.destination + (source_key - self.source)
        

        
def part1():
    seeds = [int(e) for e in lines[0][7:].split()]
    
    map_lists = []

    i = 2
    while i < len(lines):
        line = lines[i]
        if not line[0].isdigit():
            i += 1
            map_list = []
            while i < len(lines) and len(lines[i]) > 0 and lines[i][0].isdigit():
                parts = lines[i].split()
                map_list.append(Mapping(int(parts[0]), int(parts[1]), int(parts[2])))
                i += 1
            i += 1
            map_lists.append(map_list)

    result = 99999999999
    for seed in seeds:
        val = int(seed)
        for map_list in map_lists:
            for mapping in map_list:
                mapped_val = mapping.get_value(val)
                if mapped_val != val:
                    val = mapped_val
                    break
        result = min(result, val)
    return result

def part2():
    seed_ranges = [int(e) for e in lines[0][7:].split()]
    
    map_lists = []

    i = 2
    while i < len(lines):
        line = lines[i]
        if not line[0].isdigit():
            i += 1
            map_list = []
            while i < len(lines) and len(lines[i]) > 0 and lines[i][0].isdigit():
                parts = lines[i].split()
                map_list.append(Mapping(int(parts[0]), int(parts[1]), int(parts[2])))
                i += 1
            i += 1
            map_lists.append(map_list)

    result = 99999999999
    for i in range(0, len(seed_ranges), 2):
        for seed in range(int(seed_ranges[i]), int(seed_ranges[i + 1])):
            val = int(seed)
            for map_list in map_lists:
                for mapping in map_list:
                    mapped_val = mapping.get_value(val)
                    if mapped_val != val:
                        val = mapped_val
                        break
            result = min(result, val)
    return result


        


print("part 1:", part1())
print("part 2:", part2())
