def part1(file):
    with open(file) as f:
        data = f.read()
        lines = data.strip().split("\n")

    text_array = [list(line) for line in lines]

    def find_X():
        for i, row in enumerate(text_array):
            for j, char in enumerate(row):
                if char == "X":
                    yield i, j

    matches = [match for match in find_X()]

    directions = [
    (-1, -1), (-1, 0), (-1, 1),  # Up-left, Up, Up-right
    (0, -1),           (0, 1),   # Left, Right  
    (1, -1),  (1, 0),  (1, 1)    # Down-left, Down, Down-right
]

    def is_valid(row, col):
        return 0 <= row < len(text_array) and 0 <= col < len(text_array[0])

    def search_xmas(x, y):
        match_count = 0
        if is_valid(x, y):
            for direction in directions:
                if is_valid(x + direction[0], y + direction[1]) and text_array[x + direction[0]][y + direction[1]] == "M":
                    if is_valid(x + (direction[0] * 2), y + (direction[1] * 2)) and text_array[x + (direction[0] * 2)][y + (direction[1] * 2)] == "A":
                        if is_valid(x + (direction[0] * 3), y + (direction[1] * 3)) and text_array[x + (direction[0] * 3)][y + (direction[1] * 3)] == "S":
                            match_count += 1
        return match_count
    
    total = 0
    for match in matches:
        x, y = match
        match_count = search_xmas(x, y)
        total += match_count

    print(total)

def part2(file):
    with open(file) as f:
        data = f.read()
        lines = data.strip().split("\n")

    text_array = [list(line) for line in lines]

    def find_A():
        for i, row in enumerate(text_array):
            for j, char in enumerate(row):
                if char == "A":
                    yield i, j

    matches = [match for match in find_A()]

    def is_valid(row, col):
        return 0 <= row < len(text_array) and 0 <= col < len(text_array[0])

    def search_mas(x, y):
        count = 0
        if is_valid(x, y):
            # Check top-left and bottom-right diagonal pair
            if (is_valid(x-1, y-1) and is_valid(x+1, y+1)):
                pos1 = text_array[x-1][y-1]
                pos2 = text_array[x+1][y+1]
                if {pos1, pos2} == {'M', 'S'}:
                    # Check top-right and bottom-left diagonal pair  
                    if (is_valid(x-1, y+1) and is_valid(x+1, y-1)):
                        pos1 = text_array[x-1][y+1]
                        pos2 = text_array[x+1][y-1]
                        if {pos1, pos2} == {'M', 'S'}:
                            count += 1
    
        return match_count

    total = 0
    for match in matches:
        x, y = match
        match_count = search_mas(x, y)
        total += match_count

    print(total)

if __name__ == "__main__":
    part2("/Users/draki/Projects/aoc/aoc2024/day4/input.txt")