# Numeric Pattern 6

"""

1 3 5 7 9
11 13 15 17 19
21 23 25 27 29
31 33 35 37 39
41 43 45 47 49

"""

i = 0
nums = list(range(1, 50, 2))
for _ in range(5):
    j = i + 5
    row = " ".join(map(str, nums[i:j]))
    print(row)
    i = j
