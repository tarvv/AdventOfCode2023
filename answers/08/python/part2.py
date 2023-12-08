from math import lcm

directions = []
nodes = {}
with open('../../../inputs/08', 'r') as f:
    i = 0
    for line in f:
        if i == 0:
            directions = line.strip()
        if i > 1:
            line = line.split('=')
            nodes[line[0].strip()] = line[1].strip().replace('(', '').replace(')', '').replace(' ', '').split(',')
        i += 1

def solvesteps(n):
    idx = 0
    stepCnt = 0
    while n[2] != 'Z':
        if idx >= len(directions):
            idx = 0
        if directions[idx] == 'L':
            n = nodes[n][0]
        elif directions[idx] =='R':
            n = nodes[n][1]
        idx += 1
        stepCnt += 1
    return stepCnt

stepCnt = 1
for node in nodes:
    if node[2] == 'A':
        nodeSteps = 0
        idx = 0
        cNode = node
        while cNode[2] != 'Z':
            if idx >= len(directions):
                idx = 0
            if directions[idx] == 'L':
                cNode = nodes[cNode][0]
            elif directions[idx] == 'R':
                cNode = nodes[cNode][1]
            idx += 1
            nodeSteps += 1
        stepCnt = lcm(stepCnt, nodeSteps)

print(stepCnt)
#15726453850399	