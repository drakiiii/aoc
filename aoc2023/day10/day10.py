def part1(file):    
    with open(file) as f:
        lines = [line.rstrip() for line in f]

    pipes = []
    for line in lines:
        line_lst = []
        for char in line:
            line_lst.append(char)
        pipes.append(line_lst)
    
    
    start_pos = 0

    for j in range(0, len(pipes)):
        for i in range(0, len(pipes[j])):
            if pipes[i][j] == "S":
                start_pos = (i, j)
    
    print(start_pos)


    # for i in range(0, len(pipes)):
    #     if pipes[i][0] == "S":
    #         start_pos = (pipes[i][1])
    
    # def m_north():
    #     if pipes[i][0] in ("|", "L", "J"):
    #         y_pos = 1
    
    # def m_east():
    #     if pipes[i][0] in ("-", "L", "F"):
    #         x_pos = 1
    
    # def m_south():
    #     if pipes[i][0] in ("|", "F", "7"):
    #         y_pos = -1

    # def m_west():
    #     if pipes[i][0] in ("-", "J", "7"):
    #         x_pos = -1
    

part1('input.txt')