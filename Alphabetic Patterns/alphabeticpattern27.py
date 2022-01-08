print("Enter the number of rows: ")
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rows = int(input())
i = rows
while i >= 1:
    j = rows
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    k = 1
    while k <= i:
        print(alpha[i-1], end=' ')
        k += 1
    print()
    i -= 1
