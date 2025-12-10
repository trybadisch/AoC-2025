with open("input.txt", 'r') as f:
    lines = [x.strip() for x in f.readlines()]

# visualization, too big for input
'''
m_first = 0
m_last = 0

for i in lines:
    first = int(i.split(',')[0])
    last = int(i.split(',')[1])
    m_first = first if m_first < first else m_first
    m_last = last if m_last < last else m_last

print(m_first)
print(m_last)

mat = [['.' for y in range(m_first+1)] for x in range(m_last+1)]

for idx, i in enumerate(mat):
    for jdx, j in enumerate(mat[idx]):
        if str(jdx)+','+str(idx) in lines:
            mat[idx][jdx] = '#'

        print(mat[idx][jdx], end='')
    print()
'''

def part1():
    max = 0 

    for i in lines:
        x = int(i.split(',')[0])
        y = int(i.split(',')[1])

        for j in lines:
            x2 = int(j.split(',')[0])
            y2 = int(j.split(',')[1])

            x_r = (x-x2) if x > x2 else (x2-x)
            y_r = (y-y2) if y > y2 else (y2-y)

            n_max = (x_r+1) * (y_r+1)
            max = n_max if max < n_max else max

    print(max)

part1()
