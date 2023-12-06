from readFile import read_file

lines = read_file("inputs/day4.txt")

class Card:
    def __init__(self):
        self.winning_numbers = set()
        self.scratcher_numbers = []
        self.copies = 1

    def get_score(self):
        score = 0
        for num in self.scratcher_numbers:
            if num in self.winning_numbers:
                score = 1 if score == 0 else score * 2
        return score
    
    def count_matching_numbers(self):
        count = 0
        for num in self.scratcher_numbers:
            count += 1 if num in self.winning_numbers else 0
        return count
    
def create_card(line: str):
    card = Card()
    
    parts = line[line.index(':') + 2:].split('|')
    winning_numbers = parts[0].strip().split()
    scratcher_numbers = parts[1].strip().split()

    for num in winning_numbers:
        card.winning_numbers.add(int(num))
    
    for num in scratcher_numbers:
        card.scratcher_numbers.append(int(num))

    return card

def part1():
    cards = []
    for line in lines:
        cards.append(create_card(line))
    
    score = 0
    for card in cards:
        score += card.get_score()

    return score

def part2():
    cards = []
    for line in lines:
        cards.append(create_card(line))
    
    count = 0
    for i in range(len(cards)):
        card = cards[i]
        count += card.copies
        matches = card.count_matching_numbers()
        for j in range(i + 1, i + 1 + matches):
            cards[j].copies += card.copies

    return count


    

print('part 1: ', part1())
print('part 2:', part2())
