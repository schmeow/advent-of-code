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
# Part 1
""" sum = 0
for num in nums:
    for sym in syms:
        if sym[0] >= num[1] - 1 and sym[0] <= num[1] + 1:
            if sym[1] >= num[2] - 1 and sym[1] <= num[2] + len(num[0]):
                sum += int(num[0])
print(sum) """

sum = 0
for sym in syms:
    count = 0
    ratio = 1
    for num in nums:
        if sym[0] >= num[1] - 1 and sym[0] <= num[1] + 1:
            if sym[1] >= num[2] - 1 and sym[1] <= num[2] + len(num[0]):
                count+= 1
                ratio *= int(num[0])
    if count >= 2:
        sum += ratio
print(sum)

