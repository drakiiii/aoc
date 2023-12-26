import math

def part1(file):    
    with open(file) as f:
        lines = [line.rstrip() for line in f]
    
    instr = lines[0]
    d_map = []

    for i in range(1, len(lines)):
        d_map.append(lines[i].replace(",", "").replace(" =", "").replace("(", "").replace(")", "").split(" "))

    def find_in_list_of_list(mylist, char):
        for sub_list in mylist:
            if char in sub_list[0]:
                return (mylist.index(sub_list))
        raise ValueError("'{char}' is not in list".format(char = char))

    i = find_in_list_of_list(d_map, "AAA")
    loc = d_map[i][0]
    steps = 0
    
    a = 1
    
    while loc != "ZZZ":
        for index, char in enumerate(instr):
            if d_map[i][0] == loc:
                if char == "L":
                    print("instr: " + str(char))
                    print("index: " + str(index))
                    print("map: " + str(d_map[i]))
                    print("step: " + str(steps))
                    steps += 1
                    next_loc = d_map[i][1]
                    loc = next_loc
                    print("next loc: " + str(loc))
                    i = find_in_list_of_list(d_map, loc)
                    print("found next loc: " + str(i))
                    
                elif char == "R":
                    print("instr: " + str(char))
                    print("index: " + str(index))
                    print("map: " + str(d_map[i]))
                    print("step: " + str(steps))
                    steps += 1
                    next_loc = d_map[i][2]
                    loc = next_loc
                    print("next loc: " + str(loc))
                    i = find_in_list_of_list(d_map, loc)
                    print("found next loc: " + str(i))
    else:
        print(steps)
    

def part2(file):    
    with open(file) as f:
        lines = [line.rstrip() for line in f]
    
    instr = lines[0]
    d_map = []

    for i in range(1, len(lines)):
        d_map.append(lines[i].replace(",", "").replace(" =", "").replace("(", "").replace(")", "").split(" "))

    def find_in_list_of_list(mylist, char):
        for sub_list in mylist:
            if char in sub_list[0]:
                return (mylist.index(sub_list))
        raise ValueError("'{char}' is not in list".format(char = char))
    
    alocs = []
    for i in range(0, len(d_map)):
        if d_map[i][0][-1:] == "A":
            alocs.append(i)

    zlocs = []
    for i in range(0, len(d_map)):
        if d_map[i][0][-1:] == "Z":
            zlocs.append(i)
    
    t_steps = []

    for i in alocs:
        steps = 0
        loc = d_map[i][0]
        while i not in zlocs:
            for index, char in enumerate(instr):
                if d_map[i][0] == loc:
                    if char == "L":
                        steps += 1
                        next_loc = d_map[i][1]
                        loc = next_loc
                        i = find_in_list_of_list(d_map, loc)
                        
                    elif char == "R":
                        steps += 1
                        next_loc = d_map[i][2]
                        loc = next_loc
                        i = find_in_list_of_list(d_map, loc)
                        
        t_steps.append(steps)
        
    ans = math.lcm(*t_steps)

    print(ans)
