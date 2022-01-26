print("Enter the number of rows: ")
rows = int(input())
i = rows
while i >= 1:
    j = rows
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    k = 1
    while k <= i:
        print(rows-i+1, end=' ')
        k += 1
    print()
    i -= 1
    
# OUTPUT

# Enter the number of rows: 
# 5
# 1 1 1 1 1 
#   2 2 2 2 
#     3 3 3 
#       4 4 
#         5
