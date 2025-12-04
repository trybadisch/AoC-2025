with open("input.txt", 'r') as f:
    lines = [x.strip().split(',') for x in f.readlines()]

count = []

def part1():
    for i in lines[0]:

        s = int(i.split('-')[0])
        e = int(i.split('-')[1])

        for j in range(s,e+1):
            if len(str(j)) % 2 == 0:
                half = int(len(str(j))/2)

                chars = str(j)
                if chars[0:half] == chars[half:]:
                    count.append(j)

    print(sum(count))

part1()
