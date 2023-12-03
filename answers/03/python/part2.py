def getTwoOnLineProduct(lst, idx):
    mod_idx = idx
    num = []
    while lst[mod_idx-1].isdigit():
        num.append(lst[mod_idx-1])
        mod_idx = mod_idx - 1
    mod_idx = idx
    mult = int(''.join(reversed(num)))
    num = []
    while lst[mod_idx+1].isdigit():
        num.append(lst[mod_idx+1])
        mod_idx = mod_idx + 1
    return int(''.join(num)) * mult

def getSingleNum(lst, idx):
    mod_idx = idx
    num = []
    if lst[idx].isdigit():
        num.append(lst[idx])
    while lst[mod_idx-1].isdigit():
        num.append(lst[mod_idx-1])
        mod_idx = mod_idx - 1
    mod_idx = idx
    num = list(reversed(num))
    while lst[mod_idx+1].isdigit():
        num.append(lst[mod_idx+1])
        mod_idx = mod_idx + 1
    return int(''.join(num))

schematic = []
with open('../../../inputs/03', 'r') as f:
    for line in f:
        lst = []
        for c in line:
            lst.append(c)
        schematic.append(lst)

total = 0
for i, line in enumerate(schematic):
    for j, c in enumerate(line[:-1]):
        if c == '*':
            two_nAbove = not schematic[i-1][j].isdigit() and (schematic[i-1][j-1].isdigit() and schematic[i-1][j+1].isdigit()) #two numbers above
            two_nBelow = not schematic[i+1][j].isdigit() and (schematic[i+1][j-1].isdigit() and schematic[i+1][j+1].isdigit()) #two numbers below
            nAbove = schematic[i-1][j-1].isdigit() or schematic[i-1][j].isdigit() or schematic[i-1][j+1].isdigit()          #any numbers above
            nBelow = schematic[i+1][j-1].isdigit() or schematic[i+1][j].isdigit() or schematic[i+1][j+1].isdigit()          #any numbers below
            two_nBeside = schematic[i][j-1].isdigit() and schematic[i][j+1].isdigit()                                       #numbers on both side
            nBeside = schematic[i][j-1].isdigit() or schematic[i][j+1].isdigit()
            cnt = nAbove + two_nAbove + nBelow + two_nBelow + nBeside + two_nBeside
            if cnt == 2:
                if two_nAbove:
                    adder = getTwoOnLineProduct(schematic[i-1], j)
                elif two_nBeside:
                    adder = getTwoOnLineProduct(line, j)
                elif two_nBelow:
                    adder = getTwoOnLineProduct(schematic[i+1], j)
                else:
                    if nAbove and nBelow:
                        mult1 = getSingleNum(schematic[i-1], j)
                        mult2 = getSingleNum(schematic[i+1], j)
                    if nAbove and nBeside:
                        mult1 = getSingleNum(schematic[i-1], j)
                        mult2 = getSingleNum(line, j)
                    if nBeside and nBelow:
                        mult1 = getSingleNum(line, j)
                        mult2 = getSingleNum(schematic[i+1], j)
                    adder = mult1 * mult2
                total += adder
print(total)
