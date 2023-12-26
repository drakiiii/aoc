def part1(file):    
    with open(file) as f:
        lines = [line.rstrip() for line in f]

    times = list(map(int, lines[0].split()[1:]))
    distances = list(map(int, lines[1].split()[1:]))

    win_combs = []

    for x in range(0, len(times)):

        count = 0
        
        for i in range(1, times[x] + 1):
            distance_travelled = i * (times[x] - i)
            if distance_travelled > distances[x]:
                count += 1
        win_combs.append(count)

    print(win_combs[0] * win_combs[1] * win_combs[2] * win_combs[3])


def part2(file):    
    with open(file) as f:
        lines = [line.rstrip() for line in f]

    time = 44806572
    distance = 208158110501102

    win_combs = []

    count = 0
        
    for i in range(1, time + 1):
        distance_travelled = i * (time - i)
        if distance_travelled > distance:
            count += 1

    print(count)
    