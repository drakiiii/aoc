def part1(file):    

    with open(file) as f:
        data = f.read()
        lines = data.strip().split("\n")
    
    total = 0

    for line in lines[0:10]:
        count = 0
        winning_numbers = list(map(int, (line.split(':')[1].split('|')[0].split())))
        your_numbers = list(map(int, (line.split(':')[1].split('|')[1].split())))
        matched_numbers = len([x for x in your_numbers if x in winning_numbers])
        if matched_numbers > 0:
            count += matched_numbers
        total += count
    
    print(total)


def part2(file):    

    with open(file) as f:
        data = f.read()
        lines = data.strip().split("\n")
    
    n = len(lines)
    copies = [[] for _ in range(n + 1)]

    for i, line in enumerate(lines):
        game = lines[i]
        winning_numbers = list(map(int, (game.split(':')[1].split('|')[0].split())))
        your_numbers = list(map(int, (game.split(':')[1].split('|')[1].split())))

        score = 0
        for num in winning_numbers:
            if num in your_numbers:
                score += 1
        
        for j in range(i + 1, i + score + 1):
            copies[i].append(j)

    score = [0] + [1 for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in copies[i]:
            score[i] += score[j]
    
    print(copies)
    print(score)
    print(sum(score))
