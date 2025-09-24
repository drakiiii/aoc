
def is_safe(int_list):
    """Check if a list of integers is safe according to the rules"""
    if len(int_list) < 2:
        return True  # Single element or empty list is considered safe
    
    # Calculate differences between consecutive elements
    diff_list = []
    for i in range(len(int_list) - 1):
        diff_list.append(int_list[i + 1] - int_list[i])  # Note: i+1 - i for proper direction
    
    # Check if all differences are between 1 and 3 (inclusive)
    if not all(1 <= abs(diff) <= 3 for diff in diff_list):
        return False
    
    # Check if all differences have the same sign (all increasing or all decreasing)
    return all(diff > 0 for diff in diff_list) or all(diff < 0 for diff in diff_list)

def part1(file):
    with open(file) as f:
        data = f.read()
        lines = data.strip().split("\n")
    
    safe_count = 0

    for line in lines:
        # Parse the line into integers
        int_list = [int(num) for num in line.split(" ")]
        
        if is_safe(int_list):
            safe_count += 1
    
    print(safe_count)

def part2(file):
    with open(file) as f:
        data = f.read()
        lines = data.strip().split("\n")
    
    safe_count = 0

    for line in lines:
        # Parse the line into integers
        int_list = [int(num) for num in line.split(" ")]
        
        # First check if it's already safe
        if is_safe(int_list):
            safe_count += 1
        else:
            # Try removing each element to see if it can be made safe
            can_be_made_safe = False
            for i in range(len(int_list)):
                # Create a copy with element i removed
                modified_list = int_list[:i] + int_list[i+1:]
                if is_safe(modified_list):
                    can_be_made_safe = True
                    break
            
            if can_be_made_safe:
                safe_count += 1
    
    print(safe_count)



# Uncomment to test:
# part1("/Users/draki/Projects/aoc/aoc2024/day2/input.txt")
part2("/Users/draki/Projects/aoc/aoc2024/day2/input.txt")
