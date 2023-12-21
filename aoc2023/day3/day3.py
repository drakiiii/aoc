import re

def part1(file):    
    with open(file) as f:
        lines = [line.rstrip() for line in f]
    
    row_count = 0
    pos_array = []

    for line in lines[0:3]:
        col_count = 0
        nums = re.findall(r'\d+', line)
        
        for char in line:
            if char.isnumeric():
                pos_array.append([char, [row_count, col_count]])
            elif char != ".":
                pos_array.append([char, [row_count, col_count]])
            col_count += 1
        print(pos_array[0,1])
        row_count += 1

part1('input.txt')