def part1(file):    
    with open(file) as f:
        lines = [line.rstrip() for line in f]

    def find_diff(arr):
       return [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
    

    def extrapolate(hist):
        layers = [hist]
        
        while not all([x == 0 for x in layers[-1]]):
            layers.append(find_diff(layers[-1]))

        layers[-1].append(0)
        for i in range(len(layers) - 2, -1, -1):
            layers[i].append(layers[i][-1] + layers[i + 1][-1])

        return layers[0][-1]
    
    
    ans = []
    for line in lines:
        arr = list(map(int, line.split(" ")))
        ans.append(extrapolate(arr))

    print(sum(ans))


def part2(file):    
    with open(file) as f:
        lines = [line.rstrip() for line in f]

    def find_diff(arr):
       return [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
    

    def extrapolate(hist):
        layers = [hist]
        
        while not all([x == 0 for x in layers[-1]]):
            layers.append(find_diff(layers[-1]))

        layers[-1].append(0)
        for i in range(len(layers) - 2, -1, -1):
            layers[i].append(layers[i][-1] + layers[i + 1][-1])

        return layers[0][-1]
    
    
    ans = []
    for line in lines:
        arr = list(map(int, line.split(" ")[::-1]))
        ans.append(extrapolate(arr))

    print(sum(ans))

part2('input.txt')