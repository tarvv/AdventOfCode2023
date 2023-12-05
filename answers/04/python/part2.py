#I beleive this is a fairly ineneficient implementation, but it works and I got to do a recursive function for the first time since CS school
def run_copies(card_ids, t):
    next_ids = []
    for id in card_ids:
        t += 1
        win_cnt = 0
        for n in my_nums[id]:
            if n in win_nums[id]:
                win_cnt += 1
        if win_cnt:
            for cc in range(win_cnt):
                next_id = id + cc + 1
                if next_id < highest_card:
                    next_ids.append(next_id)
    if next_ids:
        return run_copies(next_ids, t)
    else:
        return t

my_nums = []
win_nums = []
total = 0
with open('../../../inputs/04', 'r') as f:
    for line in f:
        line = line.partition(':')[2]
        line = line.partition('|')
        my_nums.append(line[0].split())
        win_nums.append(line[2].split())


highest_card = len(my_nums)
copy_ids = [] #index of card; this is card number - 1
for i, card in enumerate(my_nums):
    total += 1
    win_cnt = 0
    for n in card:
        if n in win_nums[i]:
            win_cnt += 1
    if win_cnt:
        #make copy of win_cnt cards
        for cc in range(win_cnt):
            copy_ids.append(i + cc + 1)

total = run_copies(copy_ids, total)
print(total)
