# Numeric Pattern 17

"""
Desired Pattern:

0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0

"""

# Creating a list of all nums
nums = ['0']

for i in range(12):
    nums += ['1', '0']

# Printing 5 nums per loop
i = 0
for _ in range(5):
    print(" ".join(nums[i : i + 5]))
    i += 5
