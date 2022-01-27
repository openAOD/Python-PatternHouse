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
        print(i, end=' ')
        k += 1
    print()
    i -= 1
    
    
# OUTPUT
    
# Enter the number of rows: 
# 5
# 5 5 5 5 5 
#   4 4 4 4 
#     3 3 3 
#       2 2 
#         1 
