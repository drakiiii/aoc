import re

def part1(file):
    with open(file) as f:
        data = f.read()
        text = data.strip()
    
    total = 0
    # Find all mul(number,number) patterns
    matches = re.findall(r"mul\((\d+),(\d+)\)", text)
    
    for a, b in matches:
        result = int(a) * int(b)
        total += result
    print(total)
    return total

def part2(file):
    with open(file) as f:
        data = f.read()
        text = data.strip()
    
    total = 0
    enabled = True # Start enabled

    # Find all do() patterns with positions
    do_patterns = re.finditer(r"do\(\)", text)
    # Find all don't() patterns with positions  
    dont_patterns = re.finditer(r"don't\(\)", text)
    # Find all mul(number,number) patterns with positions
    mul_patterns = re.finditer(r"mul\((\d+),(\d+)\)", text)
    
    # Create a list of (position, type, match) tuples
    all_patterns = []
    for match in do_patterns:
        all_patterns.append((match.start(), 'do', match))
    for match in dont_patterns:
        all_patterns.append((match.start(), 'dont', match))
    for match in mul_patterns:
        all_patterns.append((match.start(), 'mul', match))

    # Sort by position
    all_patterns.sort(key=lambda x: x[0])

    for position, pattern_type, match in all_patterns:
        if pattern_type == 'do':
            enabled = True
        elif pattern_type == 'dont':
            enabled = False
        elif pattern_type == 'mul' and enabled:
            # Extract numbers and multiply (reuse part1 logic)
            a, b = match.groups()
            result = int(a) * int(b)
            total += result
    
    print(total)
    return total

if __name__ == "__main__":
    part2("input.txt")