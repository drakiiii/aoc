def part1(file):
    """Simulate the guard's walk and count how many tiles are visited."""
    with open(file) as f:
        data = f.read()
        lines = data.strip().split("\n")

    lines_array = []
    line_index = 0
    for line in lines:
        # Track each row as a list so we can mark visited positions.
        lines_array.append(list(line))
        for char in line:
            char_index = line.index(char)
            if char in ("<", ">", "v", "^"):
                arrow = char
                start = (char_index, line_index)
        line_index += 1
    
    def get_dir(arrow):
        if arrow == "<":
            dir = (-1, 0)
        elif arrow == ">":
            dir = (1, 0)
        elif arrow == "v":
            dir = (0, 1)
        elif arrow == "^":
            dir = (0, -1)
        return dir

    def change_dir(dir):
        if dir == (-1, 0):
            dir = (0, -1)
        elif dir == (0, -1):
            dir = (1, 0)
        elif dir == (1, 0):
            dir = (0, 1)
        elif dir == (0, 1):
            dir = (-1, 0)
        return dir  
    
    dir = get_dir(arrow)
    walk = True
    pos = start
    # Mark the starting tile before we begin marching.
    lines_array[pos[1]][pos[0]] = "X"
    while walk:
        new_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if new_pos[0] < 0 or new_pos[0] >= len(lines_array[0]) or new_pos[1] < 0 or new_pos[1] >= len(lines_array):
            walk = False
        elif lines_array[new_pos[1]][new_pos[0]] == "#":
            dir = change_dir(dir)
        else:
            pos = new_pos
            lines_array[pos[1]][pos[0]] = "X"
    
    # Count how many tiles were visited at least once.
    x_count = 0
    for line in lines_array:
        for char in line:
            if char == "X":
                x_count += 1
    print(x_count)
            
def part2(file):
    """Count the number of obstacle placements that force the guard into a loop."""
    with open(file) as f:
        data = f.read()
        lines = data.strip().split("\n")

    lines_array = []
    original_grid = []
    line_index = 0
    for line in lines:
        row = list(line)
        lines_array.append(row)
        original_grid.append(row[:])
        for char in line:
            char_index = line.index(char)
            if char in ("<", ">", "v", "^"):
                arrow = char
                start = (char_index, line_index)
        line_index += 1
    
    def get_dir(arrow):
        if arrow == "<":
            dir = (-1, 0)
        elif arrow == ">":
            dir = (1, 0)
        elif arrow == "v":
            dir = (0, 1)
        elif arrow == "^":
            dir = (0, -1)
        return dir

    def change_dir(dir):
        if dir == (-1, 0):
            dir = (0, -1)
        elif dir == (0, -1):
            dir = (1, 0)
        elif dir == (1, 0):
            dir = (0, 1)
        elif dir == (0, 1):
            dir = (-1, 0)
        return dir 
        
    # Run the original patrol once to collect candidate obstruction spots.
    visited_positions = set()
    dir = get_dir(arrow)
    walk = True
    pos = start
    visited_positions.add(pos)
    while walk:
        new_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if new_pos[0] < 0 or new_pos[0] >= len(lines_array[0]) or new_pos[1] < 0 or new_pos[1] >= len(lines_array):
            walk = False
        elif lines_array[new_pos[1]][new_pos[0]] == "#":
            dir = change_dir(dir)
        else:
            pos = new_pos
            visited_positions.add(pos)

    loop_count = 0
    for candidate in visited_positions:
        if candidate == start:
            continue
        x, y = candidate
        if original_grid[y][x] == "#":
            continue

        # Place a temporary obstruction and simulate again, tracking states.
        test_grid = [row[:] for row in original_grid]
        test_grid[y][x] = "#"
        dir = get_dir(arrow)
        walk = True
        pos = start
        seen_states = set()
        while walk:
            state = (pos, dir)
            if state in seen_states:
                loop_count += 1
                walk = False
                continue
            seen_states.add(state)
            new_pos = (pos[0] + dir[0], pos[1] + dir[1])
            if new_pos[0] < 0 or new_pos[0] >= len(lines_array[0]) or new_pos[1] < 0 or new_pos[1] >= len(lines_array):
                walk = False
            elif test_grid[new_pos[1]][new_pos[0]] == "#":
                dir = change_dir(dir)
            else:
                pos = new_pos

    print(loop_count)
