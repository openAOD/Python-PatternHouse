# Numeric Pattern 15

"""
Desired pattern:

1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
4 5 6 7 8
5 6 7 8 9

"""

for i in range(1, 6):
    print(i, end=" ")
    for _ in range(4):
        print(i + 1, end=" ")
        i += 1
    print()
