# Problem: Sum of Natural Numbers.
# link:  https://www.geeksforgeeks.org/problems/sum-of-series2811/0
# Difficulty: Basic

# n=0 sum should be 0

n = 5
var = 0
for i in range(n + 1):
    if n == 0:
        break
    else:
        var += i
print(var)

# we can use (n*(n+1))/2
