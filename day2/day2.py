with open("input.txt", 'r') as f:
    lines = [x.strip().split(',') for x in f.readlines()]

count1 = []
count2 = []

for i in lines[0]:

    t_count = []

    s = int(i.split('-')[0])
    e = int(i.split('-')[1])

    for j in range(s,e+1):

        length = len(str(j))
        chars = str(j)

        # Part 1
        if length % 2 == 0:
            half = int(length / 2)

            if chars[0:half] == chars[half:]:
                count1.append(j)
        
        # Part 2
        for str1 in range(0,length):
            for str2 in range(str1+1, length):
                len_dup = len(chars[str1:str1+str2])

                if length % len_dup == 0:
                    div = int(length / len_dup)
                    rest = str(chars[str1:str1+str2]) * div

                    if rest == chars:
                        t_count.append(j)

    for c in set(t_count):
        count2.append(c)

print(sum(count1))
print(sum(count2))
