# Numeric Pattern 2

"""
Desired Output:
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""

pattern = " ".join(map(str, list(range(1, 6))))
for _ in range(5):
    print(pattern)
