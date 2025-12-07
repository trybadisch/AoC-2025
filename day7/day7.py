with open("input.txt", 'r') as f:
    lines = [x.strip() for x in f.readlines()]

def part1():
    total = 0
    for ldx, lin in enumerate(range(0, len(lines))):

        conv = [x for x in lines[ldx]]

        for cdx, cel in enumerate(range(0, len(conv))):
            
            if conv[cdx] == 'S':
                conv[cdx] = '|'
            
            if ldx != 0:
                if conv[cdx] == '.' and lines[ldx-1][cdx] == '|':
                    conv[cdx] = '|'
                
                if conv[cdx] == '^' and lines[ldx-1][cdx] == '|':
                    conv[cdx-1] = '|'
                    conv[cdx+1] = '|'
                
                    total += 1
            
        lines[ldx] = conv

    print(total)

part1()
