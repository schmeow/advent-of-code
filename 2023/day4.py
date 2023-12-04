import sys
import re

# Part 1 

""" sum = 0
for case in range(219):
    pts = 0
    line = sys.stdin.readline().rstrip()
    wnums = re.findall("\d+", line[line.index(":"):line.index("|")])
    nums = re.findall("\d+", line[line.index("|"):])
    for num in nums:
        for wnum in wnums:
            if int(num) == int(wnum):
                if pts == 0:
                    pts += 1
                else:
                    pts *= 2
    sum += pts

print(sum) """

total = 219
cards = [1] * 219
for case in range(219):
    line = sys.stdin.readline().rstrip()
    wnums = re.findall("\d+", line[line.index(":"):line.index("|")])
    nums = re.findall("\d+", line[line.index("|"):])

    pts = 0
    for num in nums:
        for wnum in wnums:
            if int(num) == int(wnum):
                pts += 1
    for card in range(cards[case-1]):
        for pt in range(pts):
            cards[case + pt] += 1
            total += 1

print(total)