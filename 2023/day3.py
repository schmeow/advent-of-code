import re
import sys

nums = []
syms = []
full = []
for case in range(140):
    line = "." + sys.stdin.readline().rstrip() + "."
    full.append(line)
    
for l, line in enumerate(full):
    for c, char in enumerate(line):
        if char.isdigit():
            if not (full[l][c-1].isdigit()):
                sc = c
                while not (c > len(line)) and full[l][c].isdigit():
                    c += 1
                nums.append((full[l][sc:c], l, sc))
        elif char == ".":
            continue
        else:
            syms.append((l, c))
sum = 0

for num in nums:
    for sym in syms:
        if sym[0] >= num[1] - 1 and sym[0] <= num[1] + 1:
            if sym[1] >= num[2] - 1 and sym[1] <= num[2] + len(num[0]):
                sum += int(num[0])
print(sum)

# get indexes (first index) and rows (case num) of numbers 
# get indexes and rows of symbols
# if index of symbol is in the range of one behind index of num to length of num ahead of index of num 
# AND row of symbol is in the range of one behind to one ahead of row of rum
# then num is added to sum