# Problem: Palindrome Array
# link: https://www.geeksforgeeks.org/problems/perfect-arrays4645/0
# Difficulty: Basic

import copy

arr = [1, 2, 3, 2, 1]

arr1 = copy.deepcopy(arr)
i = 0
j = len(arr) - 1

while i < j:
    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j -= 1
if arr1 == arr:
    print(True)
else:
    print(False)
