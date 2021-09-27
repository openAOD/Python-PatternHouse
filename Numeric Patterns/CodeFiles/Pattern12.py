# Numeric Pattern 12

"""
Desired Output:

1 10 11 20 21
2 9  12 19 22
3 8  13 18 23
4 7  14 17 24
5 6  15 16 25

"""

x = 9
y = 1
for i in range(1, 6):
    print(i, end=" ")
    for _ in range(2):
        i += x
        print(i, end=" ")
        i += y
        print(i, end=" ")

    x -= 2
    y += 2
    print()
