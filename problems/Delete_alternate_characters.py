# Problem: Delete alternate characters
# link: https://www.geeksforgeeks.org/problems/java-delete-alternate-characters4036/0
# Difficulty: Basic

s = "GeeksforGeeks"
res = ""
for i in range(len(s)):
    if i % 2 == 0:
        res += s[i]
    else:
        s.replace("s[i]", "")
print(res)
