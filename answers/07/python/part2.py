from collections import Counter

def cScore(c):
    return {'A':'a', 'K':'b', 'Q':'c', 'J':'x', 'T':'e', '9':'f', '8':'g', '7':'h', '6':'i', '5':'j', '4':'k', '3':'l', '2':'m'}[c]

def convertedJ(hand):
    rChar = sorted(hand)[0]
    return hand.replace('x', rChar)

def bestPossible(hand):
    stripped_hand = hand.replace('x', '')
    if not stripped_hand:   
        return 'aaaaa'  #All Js: 5 of kind
    if len(stripped_hand) == 1:
        return stripped_hand * 5    #4 Js: create 5 of kind with remaining letter
    if len(stripped_hand) == 2:
        return convertedJ(hand)     #3 Js: create 4 of kind with better of remaining 2; will also return 5 of kind when remaining 2 are pair
    if len(stripped_hand) == 3:
        #pair in 3 remaining; create 4 of kind (could make full house, but 4 of kind is better)
        if len(Counter(stripped_hand).values()) == 2:
            pair = Counter(stripped_hand).most_common(1)[0][0]
            return hand.replace('x', pair)
        return convertedJ(hand) #3 of kind in 3 remaining; create 5 of kind |OR| remaining all unique; create 3 of kind from best (could make 2 pair, but 3 of kind is better)
    if len(stripped_hand) == 4:
        cnts = Counter(stripped_hand).values()
        if len(cnts) == 1:  #4 of kind in 4 remaining; create 5 of kind
            return convertedJ(hand)
        if len(cnts) == 2:
            if 3 in cnts:   #3 of kind in 4 remaining; create 4 of kind
                triple = Counter(stripped_hand).most_common(1)[0][0]
                return hand.replace('x', triple)
            if 2 in cnts:   #2 pair in 4 remaining; create full house with better value pair
                return convertedJ(hand)
        if len(cnts) == 3:  #one pair in 4 remaining; create 3 of kind
            pair = Counter(stripped_hand).most_common(1)[0][0]
            return hand.replace('x', pair) 
        if len(cnts) == 4:
            return convertedJ(hand) #all unique; create pair from best possible
    return 0

handBetDict = {}
hGroups = [[],[],[],[],[],[],[]]  #[[5ok],[4ok],[fh],[3ok],[2p],[1p],[hk]]
with open('../../../inputs/07', 'r') as f:
    for line in f:
        handBetDict[''.join(list(map(cScore, line.split()[0])))] = int(line.split()[1])

handBetDict = dict(sorted(handBetDict.items(), reverse=True))

for h in handBetDict.keys():
    if 'x' in h:
        counts = Counter(bestPossible(h)).values()
    else:
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
for grp in hGroups:
    for og_hand in grp:
        total += rank * handBetDict[og_hand]
        rank += 1
print(total)
#253907829