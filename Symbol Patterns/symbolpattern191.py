height = 5
half = height // 2
dummy = half
for i in range(0, height):
    print("*", end="")
    for j in range(0, half+1):
        if (j == abs(dummy)):
            print("*", end="")
        else:
            print(end=" ")
    print()
    dummy = dummy - 1
