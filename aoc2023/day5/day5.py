def part1(file):    

    with open(file) as f:
        data = f.read()
        lines = data.strip().split("\n")

    seeds = list(map(int, lines[0].split()[1:]))

    seed_to_soil = []
    for i in range(3, 46):
        seed_to_soil.append(list(map(int, lines[i].split())))
    
    soil_to_fert = []
    for i in range(48, 79):
        soil_to_fert.append(list(map(int, lines[i].split())))

    fert_to_water = []
    for i in range(81, 106):
        fert_to_water.append(list(map(int, lines[i].split())))
    
    water_to_light = []
    for i in range(108, 135):
        water_to_light.append(list(map(int, lines[i].split())))

    light_to_temp = []
    for i in range(137, 165):
        light_to_temp.append(list(map(int, lines[i].split())))

    temp_to_hum = []
    for i in range(167, 205):
        temp_to_hum.append(list(map(int, lines[i].split())))
    
    hum_to_loc = []
    for i in range(207, 256):
        hum_to_loc.append(list(map(int, lines[i].split())))

    locs = []

    for seed in seeds:
        conv = []
        conv.append(seed)
        for i in range(len(seed_to_soil)):
            if seed in range(seed_to_soil[i][1], seed_to_soil[i][1] + seed_to_soil[i][2]):
                conv.append(seed_to_soil[i][0] + seed - seed_to_soil[i][1])

        if len(conv) != 2:
            conv.append(seed)

        for i in range(len(soil_to_fert)):
            if conv[1] in range(soil_to_fert[i][1], soil_to_fert[i][1] + soil_to_fert[i][2]):
                conv.append(soil_to_fert[i][0] + conv[1] - soil_to_fert[i][1])
    
        if len(conv) != 3:
            conv.append(conv[1])
        
        for i in range(len(fert_to_water)):
            if conv[2] in range(fert_to_water[i][1], fert_to_water[i][1] + fert_to_water[i][2]):
                conv.append(fert_to_water[i][0] + conv[2] - fert_to_water[i][1])
                
        if len(conv) != 4:
            conv.append(conv[2])

        for i in range(len(water_to_light)):
            if conv[3] in range(water_to_light[i][1], water_to_light[i][1] + water_to_light[i][2]):
                conv.append(water_to_light[i][0] + conv[3] - water_to_light[i][1])
                
        if len(conv) != 5:
            conv.append(conv[3])
        
        for i in range(len(light_to_temp)):
            if conv[4] in range(light_to_temp[i][1], light_to_temp[i][1] + light_to_temp[i][2]):
                conv.append(light_to_temp[i][0] + conv[4] - light_to_temp[i][1])
                
        if len(conv) != 6:
            conv.append(conv[4])

        for i in range(len(temp_to_hum)):
            if conv[5] in range(temp_to_hum[i][1], temp_to_hum[i][1] + temp_to_hum[i][2]):
                conv.append(temp_to_hum[i][0] + conv[5] - temp_to_hum[i][1])
                
        if len(conv) != 7:
            conv.append(conv[5])

        for i in range(len(hum_to_loc)):
            if conv[6] in range(hum_to_loc[i][1], hum_to_loc[i][1] + hum_to_loc[i][2]):
                conv.append(hum_to_loc[i][0] + conv[6] - hum_to_loc[i][1])
                locs.append(hum_to_loc[i][0] + conv[6] - hum_to_loc[i][1])
                
        if len(conv) != 8:
            conv.append(conv[6])
            locs.append(conv[6])        

    print(min(locs))


def part2(file):    

    import re

    with open(file) as f:
        lines = f.read().strip().split("\n")

    raw_seeds = list(map(int, lines[0].split(" ")[1:]))
    seeds = [
        (raw_seeds[i], raw_seeds[i+1])
        for i in range(0, len(raw_seeds), 2)
    ]

    # Generate all the mappings
    maps = []

    i = 2
    while i < len(lines):
        catA, _, catB = lines[i].split(" ")[0].split("-")
        maps.append([])

        i += 1
        while i < len(lines) and not lines[i] == "":
            dstStart, srcStart, rangeLen = map(int, lines[i].split())
            maps[-1].append((dstStart, srcStart, rangeLen))
            i += 1

        maps[-1].sort(key=lambda x: x[1])

        i += 1


    # Ensure that all mappings are disjoint
    for m in maps:
        for i in range(len(m)-1):
            if not m[i][1] + m[i][2] <= m[i+1][1]:
                print(m[i], m[i+1])


    def remap(lo, hi, m):
        # Remap an interval (lo,hi) to a set of intervals m
        ans = []
        for dst, src, R in m:
            end = src + R - 1
            D = dst - src  # How much is this range shifted

            if not (end < lo or src > hi):
                ans.append((max(src, lo), min(end, hi), D))

        for i, interval in enumerate(ans):
            l, r, D = interval
            yield (l + D, r + D)

            if i < len(ans) - 1 and ans[i+1][0] > r + 1:
                yield (r + 1, ans[i+1][0] - 1)

        # End and start ranges can use some love
        if len(ans) == 0:
            yield (lo, hi)
            return

        if ans[0][0] != lo:
            yield (lo, ans[0][0] - 1)
        if ans[-1][1] != hi:
            yield (ans[-1][1] + 1, hi)


    locs = []

    ans = 1 << 60

    for start, R in seeds:
        cur_intervals = [(start, start + R - 1)]
        new_intervals = []

        for m in maps:
            for lo, hi in cur_intervals:
                for new_interval in remap(lo, hi, m):
                    new_intervals.append(new_interval)

            cur_intervals, new_intervals = new_intervals, []

        for lo, hi in cur_intervals:
            ans = min(ans, lo)


    print(ans)
    