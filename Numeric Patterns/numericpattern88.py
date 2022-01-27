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
        print(k, end=' ')
        k += 1
    print()
    i -= 1
    
# OUTPUT

# Enter the number of rows: 
# 5
# 1 2 3 4 5 
#   1 2 3 4 
#     1 2 3 
#       1 2 
#         1 
