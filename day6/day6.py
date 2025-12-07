import math

with open("input.txt", 'r') as f:
    lines = [x.strip() for x in f.readlines()]

op = [x for x in lines[-1].split(' ') if len(x.strip()) != 0]

nums = lines[0:-1]

def part1():
    total = 0
    for ndx, num in enumerate(range(0, len(op))):
        calc = []
        for ldx, lin in enumerate(range(0, len(nums))):
            line = [x for x in nums[ldx].split(' ') if len(x.strip()) != 0]
            if len(line[ndx].strip()) != 0:
                calc.append(int(line[ndx]))

        if op[ndx] == '+':
            total += sum(calc)
        
        elif op[ndx] == '*':
            total += math.prod(calc)
        
    print(total)

part1()
