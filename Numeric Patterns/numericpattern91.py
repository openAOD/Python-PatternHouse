print("Enter the number of rows: ")
rows = int(input())
i = rows
count=0
while i >= 1:
    j = rows
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    k = 1
    flag = rows
    while k <= i:
        print(flag-count, end=' ')
        k += 1
        flag-=1
    count+=1

    print()
    i -= 1
    
    
# OUTPUT
    
# Enter the number of rows: 
# 5
# 5 4 3 2 1 
#   4 3 2 1 
#     3 2 1 
#       2 1 
#         1 
