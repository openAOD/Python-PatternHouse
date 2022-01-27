print("Enter the number of rows: ")
rows = int(input())
i = rows
count=0
flag = 1
while i >= 1:
    j = rows
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    k = 1
    
    while k <= i:
        print(flag, end=' ')
        k += 1
        flag+=1
    count+=1

    print()
    i -= 1
    
    
# OUTPUT

# Enter the number of rows: 
# 5
# 1 2  3  4  5 
#   6  7  8  9 
#     10 11 12 
#        13 14 
#           15 
