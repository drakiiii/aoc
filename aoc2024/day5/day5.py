def part1(file):
    with open(file) as f:
        data = f.read()
        lines = data.strip().split("\n")

    page_rules = [tuple(map(int, line.split("|"))) for line in lines if "|" in line]
    update_order = [tuple(map(int, line.split(","))) for line in lines if "," in line]
    total_correct = 0

    for update in update_order:
        bad_update = False
        for num_a, num_b in page_rules:
            if num_a in update and num_b in update:
                index_a = update.index(num_a)
                index_b = update.index(num_b)
                if index_a < index_b:
                    continue
                else:
                    bad_update = True
                    break
            else:
                continue
        
        if bad_update == False:
            middle_value = len(update) // 2
            total_correct += update[middle_value]

    print(total_correct)

def part2(file):
    with open(file) as f:
        data = f.read()
        lines = data.strip().split("\n")

    page_rules = [tuple(map(int, line.split("|"))) for line in lines if "|" in line]
    update_order = [tuple(map(int, line.split(","))) for line in lines if "," in line]
    total_correct = 0

    for update in update_order:
        print("--------------------------------")
        print(f"update: {update}")
        bad_update = False
        for num_a, num_b in page_rules:
            if num_a in update and num_b in update:
                index_a = update.index(num_a)
                index_b = update.index(num_b)
                if index_a < index_b:
                    continue
                else:
                    bad_update = True
                    print("--------------------------------")
                    print(f"num_a {num_a} @ index {index_a} is after num_b {num_b} @ index {index_b}")
            else:
                continue
        
        if bad_update == True:
            middle_value = len(update) // 2
            total_correct += update[middle_value]

    # print(total_correct)

if __name__ == "__main__":
    part2("/Users/draki/Projects/aoc/aoc2024/day5/input.txt")