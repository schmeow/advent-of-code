import re
import sys

# Part One

""" sum = 0
for case in range(1000):
    word = sys.stdin.readline().rstrip()
    nums = re.findall("\d+", " ".join(word))
    value = int(nums[0] + nums[len(nums) - 1])
    sum = sum + value

print(sum) """

# Final

sum = 0
numlist = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for case in range(1000):
    word = sys.stdin.readline().rstrip()
    nums = []
    for i,letter in enumerate(word):
        if letter.isdigit():
            nums.append(letter)
        for num in numlist:
            if word[i:].startswith(num):
                nums.append(str(numlist.index(num)))
    value = int(nums[0] + nums[len(nums)-1])
    sum = sum + value
print(sum)
