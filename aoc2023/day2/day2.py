def part1(file):    
    with open(file) as f:
        lines = [line.rstrip() for line in f]

    count = 0

    blue_max = 14
    red_max = 12
    green_max = 13


    for line in lines:
        blue = []
        red = []
        green = []
        colour_set = []
        
        game_no = (line.split(':')[0]).split(' ')[1]
        line = line.split(': ', 1)[-1]
        line = line.replace(';', ',')
        line = line.split(', ')

        for x in line:
            if " blue" in x:
                x = x.replace(" blue", "b")
                blue.append(int(x[:-1]))
                max_blue = max(blue)
        
                if max_blue > blue_max:
                    colour_set.append(True)

            if " red" in x:
                x = x.replace(" red", "r")
                red.append(int(x[:-1]))
                max_red = max(red)
                if max_red > red_max:
                    colour_set.append(True)
            
            if " green" in x:
                x = x.replace(" green", "g")
                green.append(int(x[:-1]))
                max_green = max(green)
                if max_green > green_max:
                    colour_set.append(True)

        if any(colour_set):
            exit
        
        else:
            count += int(game_no)

    print(count)


def part2(file):    
    with open(file) as f:
        lines = [line.rstrip() for line in f]

    total_power = 0

    for line in lines:
        blue = []
        red = []
        green = []
        colour_set = []
        
        game_no = (line.split(':')[0]).split(' ')[1]
        line = line.split(': ', 1)[-1]
        line = line.replace(';', ',')
        line = line.split(', ')

        for x in line:
            if " blue" in x:
                x = x.replace(" blue", "b")
                blue.append(int(x[:-1]))
                max_blue = max(blue)
        
            if " red" in x:
                x = x.replace(" red", "r")
                red.append(int(x[:-1]))
                max_red = max(red)
            
            if " green" in x:
                x = x.replace(" green", "g")
                green.append(int(x[:-1]))
                max_green = max(green)

        colour_set.append(max_blue)
        colour_set.append(max_red)
        colour_set.append(max_green)

        power = (colour_set[0] * colour_set[1] * colour_set[2])
        total_power += power
            
    print(total_power)
