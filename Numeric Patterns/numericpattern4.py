# Numeric Pattern 4

"""
Desired Pattern:

5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1

"""

pattern = " ".join(map(str, list(range(5, 0, -1))))
for _ in range(5):
    print(pattern)
