def part1(file):
    """Depth-first search over addition/multiplication combinations (Part 1)."""
    with open(file) as f:
        data = f.read()
        lines = data.strip().split("\n")

    total_calibration = 0
    for line in lines:
        parts = line.split()
        target = int(parts[0][:-1])
        numbers = [int(x) for x in parts[1:]]

        def can_reach(value, idx):
            # Explore all ways to reach the target using + and *.
            if idx == len(numbers):
                return value == target
            next_val = numbers[idx]
            if can_reach(value + next_val, idx + 1):
                return True
            if can_reach(value * next_val, idx + 1):
                return True
            return False

        if can_reach(numbers[0], 1):
            total_calibration += target
    
    print(total_calibration)
    

def part1(file):
    """Extended search including concatenation (intended Part 2 logic)."""
    with open(file) as f:
        data = f.read()
        lines = data.strip().split("\n")

    total_calibration = 0
    for line in lines:
        parts = line.split()
        target = int(parts[0][:-1])
        numbers = [int(x) for x in parts[1:]]

        def can_reach(value, idx):
            # Explore +, *, and digit-concatenation paths.
            if idx == len(numbers):
                return value == target
            next_val = numbers[idx]
            if can_reach(int(str(value) + str(next_val)), idx + 1):
                return True
            if can_reach(value + next_val, idx + 1):
                return True
            if can_reach(value * next_val, idx + 1):
                return True
            return False

        if can_reach(numbers[0], 1):
            total_calibration += target

    print(total_calibration)

            