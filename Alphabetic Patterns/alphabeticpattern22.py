size = int(input("Number of Rows: "))
for i in range(size):
    for j in range(1, size - i):
        print(" ", end="")
    for k in range(i + 1):
        print(chr(65 + k), end="")
    print() 