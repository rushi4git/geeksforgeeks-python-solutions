# Problem: Swap Kth elements
# link: https://www.geeksforgeeks.org/problems/swap-kth-elements5500/0
# # Difficulty: Basic
arr = [45, 15, 81, 19, 51, 64, 36, 99, 72]
k = 9
print(arr)
for i in range(len(arr)):
    if i + 1 == k:
        arr[i], arr[-k] = arr[-k], arr[i]
print(arr)
