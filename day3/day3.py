with open("input.txt", 'r') as f:
    lines = [x.strip() for x in f.readlines()]

count = []

def part1():
    for i in lines:
        max = 0
        for idj, j in enumerate(i):
            for k in i[idj+1:]:
                max = int(j+k) if max < int(j+k) else max
        count.append(max)

    print(sum(count))

part1()
