# Problem: Check if string is isogram or not
# link: https://www.geeksforgeeks.org/problems/check-if-a-string-is-isogram-or-not-1587115620/0
# Difficulty: Basic


# Function to check if a string is Isogram or not.
def isIsogram(s):
    # Your code here
    di = {}
    for i in s:
        if i in di:
            return 0
        else:
            di[i] = 1
    return 1


print(isIsogram("machine"))


# # n^2 method
# def isIsogram(s):
#     for i in range(len(s)):
#         for j in range(i + 1, len(s)):
#             if s[i] == s[j]:
#                 return 0
#     return 1


# print(isIsogram("machinem"))
