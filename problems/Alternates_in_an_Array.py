# Problem: Alternates in an Array.
# link:  https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqa29RLVhmWmQ3bXZQYUVBM09lZEwzSlFiQjFvQXxBQ3Jtc0trY2tNR0lBY3E4SE9YaVNxaE9kRFVVQ1MwMmVaU0ZKOWdsVU5NMV9DRFI1aE0yVzRaa0JxSUlGZVV5alRFSmtnMFBsVGQ5ZHYySm10bXJuaGhBRTg2QnpyRE1LN282Z2EwMG40NFg5Ym5wUGs5Wl9ZQQ&q=https%3A%2F%2Fwww.geeksforgeeks.org%2Fproblems%2Fprint-alternate-elements-of-an-array%2F1%3Fpage%3D1%26category%3DArrays%26difficulty%3DBasic%26sortBy%3Dsubmissions&v=rsubrskHQ4s
# Difficulty: Basic

arr = [1, 2, 3, 4, 5, 6]
output = []

for i in range(len(arr)):
    if i % 2 == 0:
        output.append(arr[i])
    else:
        continue

print("Value of output", output)
