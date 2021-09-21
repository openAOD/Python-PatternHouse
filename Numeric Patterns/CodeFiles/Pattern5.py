# Numeric Pattern 5

"""

1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25

"""
i = 0
nums = list(range(1, 26))
for _ in range(5):
    j = i + 5
    row = " ".join(map(str, nums[i:j]))
    print(row)
    i = j
