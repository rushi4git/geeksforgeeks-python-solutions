# Problem: Replace_all_0s_with_5
# link:  https://www.geeksforgeeks.org/problems/replace-all-0s-with-5/0
# Difficulty: Basic

n = 1004
# o/p: 1554
res = ""
str_n = str(n)

for i in str_n:
    if i == "0":
        res = res + "5"
    else:
        res += i

print(res)
