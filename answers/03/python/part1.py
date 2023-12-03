def isAdj(s, l, strt, end):
    validlist = ['*', '+', '=', '%', '-', '#', '@', '/', '&', '$']
    chkfrom = strt - 1 if strt else 0   #chkfrom won't be negative
    chkto = end + 1 if (end == len(s[l]) - 1) else end + 2 #chkto won't be larger than the line length
    chksym = []
    if strt:    #left
        chksym.append(s[l][strt-1])
    if end != len(s[l]) - 1:    #right
        chksym.append(s[l][end+1])
    if l:  #not first line
        for char in s[l-1][chkfrom:chkto]:
            chksym.append(char)
    if l != len(s)-1: #not last line
        for char in s[l+1][chkfrom:chkto]:
            chksym.append(char)
    
    for char in chksym:
        if char in validlist:
            return True
    return False

schematic = []
with open('../../../inputs/03', 'r') as f:
    for line in f:
        lst = []
        for c in line:
            lst.append(c)
        schematic.append(lst)


curr_num = []
strt_idx = 0
total = 0
for i, line in enumerate(schematic):
    for j, c in enumerate(line[:-1]):
        if c.isdigit(): #is a digit
            if not curr_num:    #first digit in num
                strt_idx = j
            curr_num.append(c)
            if not line[j+1].isdigit():   #last digit in num
                num = int(''.join(curr_num))
                curr_num = []
                if isAdj(schematic, i, strt_idx, j):
                    total += num
print(total)