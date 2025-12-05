with open("input.txt", 'r') as f:
    lines = [x.strip() for x in f.readlines()]

ranges = []
ingredients = []
fresh = []

for i in lines:
    if '-' in i:
        ranges.append(i)
    else:
        ingredients.append(i)

ingredients.remove("")

def part1():
    for r in ranges:
        s = int(r.split('-')[0])
        e = int(r.split('-')[1])

        for i in ingredients:
            if int(i) >= s and int(i) <= e:
                fresh.append(i)

    fresh_u = set(fresh)
    print(len(fresh_u))

part1()
