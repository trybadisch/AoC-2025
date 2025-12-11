with open("input.txt", 'r') as f:
    lines = [x.strip() for x in f.readlines()]

def part1():
    count = []
    for i in lines:
        max_ = 0
        for idj, j in enumerate(i):
            for k in i[idj+1:]:
                max_ = int(j+k) if max_ < int(j+k) else max_
        count.append(max_)

    print(sum(count))

def part2():
    count = []
    for i in lines:
        max_ = ""
        ind = 0

        for r in range(1,12+1):

            try:
                m_num = max([int(x) for x in i[ind:-(12-r)]])
            except:
                m_num = max([int(x) for x in i[ind:]])

            max_ += str(m_num)
            ind += i[ind:].index(str(m_num))+1

        count.append(int(max_))

    print(sum(count))

part1()
part2()
