def part1(file):
    """Compute total distance between sorted lists of location IDs."""
    with open(file) as f:
        data = f.read()
        lines = data.strip().split("\n")
    # Separate values into the left and right lists before sorting.
    left_list = []
    right_list = []
    distance_list = []

    for line in lines:
        left_list.append(int(line[:5]))
        right_list.append(int(line[-5:]))

    left_list.sort()
    right_list.sort()

    for i in range(0, len(left_list)):
        # Pairwise absolute differences after sorting give the distances.
        distance_list.append(abs(left_list[i] - right_list[i]))

    print(sum(distance_list))

def part2(file):
    """Compute similarity score using counts of right-list occurrences."""
    with open(file) as f:
        data = f.read()
        lines = data.strip().split("\n")
    
    # Build the lists of identifiers for repeated counting later.
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
        # Each occurrence contributes its value multiplied by the count on the right.
        similarity_score += num * count

    print(similarity_score)
