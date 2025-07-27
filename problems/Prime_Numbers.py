# Problem: Prime Numbers
# link: https://www.geeksforgeeks.org/problems/prime-number2314/0
# # Difficulty: Basic

n = 25
start = 2
end = int(n**0.5)
if n == 1:
    print(False)
if n == 2:
    print(True)
else:
    for i in range(start, end + 1):
        if n % i == 0:
            print(False)
            break
    else:
        print(True)
