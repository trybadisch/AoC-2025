with open("input.txt", 'r') as f:
    lines = [x.strip().split(',') for x in f.readlines()]

def part1():
    count = []
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

def part2():
    count = []
    for i in lines[0]:

        t_count = []

        s = int(i.split('-')[0])
        e = int(i.split('-')[1])

        for j in range(s,e+1):
            length = len(str(j))
            chars = str(j)

            for str1 in range(0,length):
                for str2 in range(str1+1, length):
                    l_str = len(chars)
                    l_dup = len(chars[str1:str1+str2])

                    if l_str % l_dup == 0:
                        div = int(l_str / l_dup)
                        rest = str(chars[str1:str1+str2]) * div

                        if rest == chars:
                            t_count.append(j)

        for c in set(t_count):
            count.append(c)

    print(sum(count))

part1()
part2()
