# Problem: Alternates in an Array.
# link:  https://www.geeksforgeeks.org/problems/print-alternate-elements-of-an-array

arr = [1, 2, 3, 4, 5, 6]
output = []

for i in range(len(arr)):
    if i % 2 == 0:
        output.append(arr[i])
    else:
        continue

print("Value of output", output)
