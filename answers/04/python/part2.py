my_nums = []
win_nums = []
with open('../../../inputs/04', 'r') as f:
    for line in f:
        line = line.partition(':')[2]
        line = line.partition('|')
        my_nums.append(line[0].split())
        win_nums.append(line[2].split())

copies = []
total = 0
for i, card in enumerate(my_nums):
    win_cnt = 0
    for n in card:
        if n in win_nums[i]:
            win_cnt += 1
    if win_cnt:
        total += 2**(win_cnt-1)

print(total)
