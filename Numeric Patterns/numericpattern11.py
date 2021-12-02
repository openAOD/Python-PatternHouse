# Numeric Pattern 11

"""

1 6 11 16 21
2 7 12 17 22
3 8 13 18 23
4 9 14 19 24
5 10 15 20 25

"""

for i in range(1, 6):
    print(i, end=" ")
    for _ in range(4):
        x = i + 5
        print(x, end=" ")
        i = x
    print()

