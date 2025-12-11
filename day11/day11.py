with open("input.txt", 'r') as f:
    lines = [x.strip() for x in f.readlines()]

nodes = [[y.split(' ') for y in lines[idx].split(': ')] for idx,x in enumerate(lines)]

count = 0

def part1(dev):
    global count
    for i in nodes:
        if i[0][0] == dev:
            for j in i[1]:
                if j == "out":
                    count += 1
                else:
                    part1(j)

part1("you")
print(count)
