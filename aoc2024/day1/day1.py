def part1(file):
    with open(file) as f:
        data = f.read()
        lines = data.strip().split("\n")

    left_list = []
    right_list = []
    distance_list = []

    for line in lines:
        left_list.append(int(line[:5]))
        right_list.append(int(line[-5:]))

    left_list.sort()
    right_list.sort()

    for i in range(0, len(left_list)):
        distance_list.append(abs(left_list[i] - right_list[i]))

    print(sum(distance_list))

def part2(file):
    with open(file) as f:
        data = f.read()
        lines = data.strip().split("\n")
    
    left_list = []
    right_list = []

    for line in lines:
        left_list.append(int(line[:5]))
        right_list.append(int(line[-5:]))
    
    count_list = []
    
    for num in left_list:
        int_count = []
        int_count.append(num)
        count = right_list.count(num)
        int_count.append(count)
        count_list.append(int_count)

    similarity_score = 0

    for num, count in count_list:
        similarity_score += num * count

    print(similarity_score)


