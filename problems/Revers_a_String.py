# Problem: Reverse a String
# link: https://www.geeksforgeeks.org/problems/java-reverse-a-string0416/0
# # Difficulty: Basic

s = "GeeksforGeeks"
start = len(s) - 1
end = -1
step = -1
res = ""
for i in range(start, end, step):
    res = res + s[i]

print(res)
