# Problem: Count type of Characters.
# link: https://www.geeksforgeeks.org/problems/count-type-of-characters3635/0
# Difficulty: Basic

"""
S = "#GeeKs01fOr@gEEks07"
Output:
5
8
4
2
Explanation: There are 5 uppercase characters,8 lowercase characters, 4 numeric charactersand 2 special characters."""

s = "#GeeKs01fOr@gEEks07"
spl_chr = ["#", "@", "!", "$", "%", "&", "*"]
upper_cnt = 0
lwr_cnt = 0
num_cnt = 0
spl_cnt = 0
for i in s:
    if i.isupper():
        upper_cnt += 1
    elif i.islower():
        lwr_cnt += 1
    elif i.isnumeric():
        num_cnt += 1
    else:
        spl_cnt += 1
print(upper_cnt)
print(lwr_cnt)
print(num_cnt)
print(spl_cnt)
