with open("input.txt", 'r') as f:
    lines = [x.strip() for x in f.readlines()]

lim = 99
cur = 50
count = 0

def part1(cur, count):
    for i in lines:
        if i[0] == 'L':
            cur = cur - int(i[1:])
            while cur < 0:
                cur = (lim+1) + cur

        elif i[0] == 'R':
            cur = cur + int(i[1:])
            while cur > lim:
                cur = cur - (lim+1)

        if cur == 0:
            count += 1
    print(count)

part1(cur, count)
