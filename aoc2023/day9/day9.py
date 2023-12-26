def part1(file):    
    with open(file) as f:
        lines = [line.rstrip() for line in f]

    def checkList(lst):
        ele = lst[0]
        chk = True

        for item in lst:
            if ele != item:
                chk = False
                break

        if chk == True:
            return True
        else:
            return False
 

    def find_diff(line):
        while checkList(line) == False:
            new_line = []
            for i in range(0, len(line) - 1):
                diff = line[i + 1] - line[i]
                new_line.append(diff)
            line = [[a for a in line], [b for b in new_line]]
            new_line
        return line

    for line in lines[0:1]:
        line = list(map(int, line.split(" ")))
        while checkList(line) is False:
            line = find_diff(line)
        

part1('input.txt')