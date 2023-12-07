inlines = []
with open('../../../inputs/06', 'r') as f:
    for line in f:
        inlines.append(line)

times = list(map(int, inlines[0].removeprefix('Time:').split()))
dists = list(map(int, inlines[1].removeprefix('Distance:').split()))

margErr = 1
for i, race_ms in enumerate(times):
    win_cnt = 0
    hold_ms = int(race_ms / 2)
    res_mm = (race_ms - hold_ms) * hold_ms
    while res_mm > dists[i]:
        win_cnt += 1
        hold_ms -= 1
        res_mm = (race_ms - hold_ms) * hold_ms
    win_cnt *= 2
    if not race_ms % 2:
        win_cnt -= 1
    margErr *= win_cnt

print(margErr)
#6209190
