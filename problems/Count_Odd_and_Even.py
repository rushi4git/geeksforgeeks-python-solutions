# Problem: Count Odd and Even.
# link:  https://www.geeksforgeeks.org/problems/count-odd-even/0
# Difficulty: Basic

arr = [2, 4, 6, 8]
count = 0
count1 = 0

for i in arr:
    if i % 2 == 0:
        count += 1
for j in arr:
    if j % 2 == 0:
        continue
    else:
        count1 += 1

print(count, count1)
