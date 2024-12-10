# Part 1

''' 
list1 = []
list2 = []
num = 1000
for case in range(num):
    pair = input()
    list1.append(int(pair[:pair.index(' ')]))
    list2.append(int(pair[pair.index(' ') + 3:]))

list1 = sorted(list1)
list2 = sorted(list2)

print(list1, list2)

diff = 0
for case in range(num):
    diff += abs(list1[case]-list2[case])

print(diff)
'''

# Part 2

list1 = []
list2 = []
num = 1000
for case in range(num):
    pair = input()
    list1.append(int(pair[:pair.index(' ')]))
    list2.append(int(pair[pair.index(' ') + 3:]))

list1 = sorted(list1)
list2 = sorted(list2)

sim = 0
for num in list1:
    t = 0
    listt = list2.copy()
    while num in listt:
        t += 1
        listt.remove(num)
    sim += num * t

print(sim)