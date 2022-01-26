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
    
    while k <= i:
        print(k+count, end=' ')
        k += 1
    count+=1

    print()
    i -= 1
    
    
# Enter the number of rows: 
# 5
# 1 2 3 4 5 
#   2 3 4 5 
#     3 4 5 
#       4 5 
#         5 
