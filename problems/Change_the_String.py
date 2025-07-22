# Problem: Change the string
# link:  https://www.geeksforgeeks.org/problems/change-the-string3541/0
# Difficulty: Basic

s = "CabCDe"
# o/p: 'abcd'
res = ""


if s[0].isupper():
    res = res + s.upper()
else:
    res = res + s.lower()

print(res)
