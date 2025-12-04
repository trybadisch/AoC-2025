with open("input.txt", 'r') as f:
    lines = [x.strip() for x in f.readlines()]

# matrix[ver][hor]
mat = [[y for y in lines[idx]] for idx,x in enumerate(lines)]

width = len(lines[0])
height = len(lines)

dir = [
    [-1,-1], [-1,0], [-1,+1],
    [0,-1], [0,+1],
    [+1,-1], [+1,0], [+1,+1]
]

def solve(part):
    total = 0

    def check(y, x):
        counter = 0
        for d in dir:
            dy = y+d[0]; dx = x+d[1]

            if (dy >= 0 and dy < height) and (dx >= 0 and dx < width):
                if mat[dy][dx] == '@':
                    counter += 1
        
        if part == 1:
            return 1 if counter < 4 else 0
        
        elif part == 2:
            if counter < 4:
                mat[y][x] = 'x'
                return 1
            else:
                return 0

    for y, ver in enumerate(mat):
        for x, hor in enumerate(ver):
            if mat[y][x] == '@':
                total += check(y, x)

    return(total)

part1 = solve(part=1)
print(part1)

p2_total = 0
flag = 1

while flag == 1:
    part2 = solve(part=2)
    p2_total += part2

    flag = 1 if part2 != 0 else 0

print(p2_total)
