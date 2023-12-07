inlines = []
with open('../../../inputs/06', 'r') as f:
    for line in f:
        inlines.append(line)

race_ms = int(inlines[0].removeprefix('Time:').strip().replace(' ', ''))
best_mm = int(inlines[1].removeprefix('Distance:').strip().replace(' ', ''))
win_cnt = 0
hold_ms = int(race_ms / 2)  #half race time holding results in farthest distance
res_mm = (race_ms - hold_ms) * hold_ms  #get first result (farthest possible)
#should really use a greedy algorithm from here, but this is way quicker for me to implement and only needs to run once ever
while res_mm > best_mm:     #run each possible from the best possible until not beating current best
    win_cnt += 1
    hold_ms -= 1
    res_mm = (race_ms - hold_ms) * hold_ms
print(win_cnt * 2 - 1)    #I know it's even, so subtract 1 from result
