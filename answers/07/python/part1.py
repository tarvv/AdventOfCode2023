from collections import Counter

def cScore(c):
    return {'A':'a', 'K':'b', 'Q':'c', 'J':'d', 'T':'e', '9':'f', '8':'g', '7':'h', '6':'i', '5':'j', '4':'k', '3':'l', '2':'m'}[c]

handBetDict = {}
hGroups = [[],[],[],[],[],[],[]]  #[[5ok],[4ok],[fh],[3ok],[2p],[1p],[hk]]
with open('../../../inputs/07', 'r') as f:
    for line in f:
        handBetDict[''.join(list(map(cScore, line.split()[0])))] = int(line.split()[1])

handBetDict = dict(sorted(handBetDict.items(), reverse=True))
for h in handBetDict.keys():
    counts = Counter(h).values()
    match len(counts):
        case 1:     #5 of a kind - [5]
            hGroups[6].append(h)
        case 2:     #4 of a kind - [4,1]; full house - [3,2]
            hGroups[5].append(h) if 4 in counts else hGroups[4].append(h)
        case 3:     #3 of a kind - [3,1,1]; 2 pair - [2,2,1]
            hGroups[3].append(h) if 3 in counts else hGroups[2].append(h)
        case 4:     #1 pair - [2,1,1,1]
            hGroups[1].append(h)
        case 5:     #High card - [1,1,1,1,1]
            hGroups[0].append(h)

total = 0
rank = 1
for g in hGroups:
    for hand in g:
        total += rank * handBetDict[hand]
        rank += 1
print(total)
#253205868