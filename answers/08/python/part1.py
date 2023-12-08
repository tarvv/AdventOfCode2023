
directions = []
nodes = {}
# lines = []
with open('../../../inputs/08', 'r') as f:
    i = 0
    for line in f:
        if i == 0:
            directions = line.strip()
        # directions = list(l)
        if i > 1:
            line = line.split('=')
            nodes[line[0].strip()] = line[1].strip().replace('(', '').replace(')', '').replace(' ', '').split(',')
        i += 1

node = 'AAA'
stepCnt = 0
idx = 0
while node != 'ZZZ':
    if idx >= len(directions):
        idx = 0
    if directions[idx] == 'L':
        node = nodes[node][0]
    elif directions[idx] =='R':
        node = nodes[node][1]
    else:
        print(f'shit broke\nnode {node} | stepCnt {stepCnt} | idx {idx} | dir {directions[idx]}')
        break
    stepCnt += 1
    idx += 1
print(stepCnt)