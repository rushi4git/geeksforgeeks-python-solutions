# Problem: Count of camel case Characters.
# link: https://www.geeksforgeeks.org/problems/find-the-camel3348/0
# Difficulty: Basic

# Given a string. Count the number of Camel Case characters in it.

s = "abcd"
count = 0

for i in s:
    if i.isupper():
        count += 1
print(count)
