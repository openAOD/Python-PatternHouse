# Numeric Pattern 7

"""

2 4 6 8 10
12 14 16 18 20
22 24 26 28 30
32 34 36 38 40
42 44 46 48 50

"""

i = 0
nums = list(range(2, 52, 2))

for _ in range(5):
    j = i + 5
    row = " ".join(map(str, nums[i:j]))
    print(row)
    i = j
