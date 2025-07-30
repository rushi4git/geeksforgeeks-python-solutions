# Problem: Array Search
# link: https://www.geeksforgeeks.org/problems/search-an-element-in-an-array-1587115621/0
# Difficulty: Basic

arr = [1, 2, 3, 4]
x = 6

if x not in arr:
    print(-1)
else:
    for i in range(len(arr)):
        if arr[i] == x:
            print(i)
            break
