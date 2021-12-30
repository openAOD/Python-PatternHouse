height = 5
width = 2 * height - 1
n = width // 2
for i in range(0, height):
    for j in range(0, width + 1):
        if j == n or j == (width - n) or (i == (height // 2) and n < j < (width - n)):
            print("*", end="")
        else:
            print(end=" ")
    print()
    n = n - 1
