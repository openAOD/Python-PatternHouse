# Numeric Pattern 12

"""
Desired Output:

5 10 15 20 25
4  9 14 19 24
3  8 13 18 23
2  7 12 17 22
1  6 11 16 21
"""

x = 5
for i in range(5, 0, -1):
    j = i
    for _ in range(5):
        print(j, end=" ")
        j += x
    print()
