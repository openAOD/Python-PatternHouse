# Numeric Pattern 16

"""
Desired Pattern:

1  3  5  7  9
3  5  7  9 11
5  7  9 11 13
7  9 11 13 15
9 11 13 15 17

"""

for i in range(1, 10, 2):
    print(i, end=" ")
    for _ in range(4):
        print(i + 2, end = " ")
        i += 2
    print()
