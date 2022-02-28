#18 - Numeric Pattern 
nums = ['1']

for i in range(12):
    nums += ['0', '1']

# Printing 5 nums per loop
i = 0
for _ in range(5):
    print(" ".join(nums[i : i + 5]))
    i += 5 