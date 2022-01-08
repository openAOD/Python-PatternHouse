print("Enter the number of rows: ")
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rows = int(input())
i = rows
while i >= 1:
    j = rows
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    k = 0
    count = rows - 1
    while k < i:
        print(alpha[count], end=' ')
        count = count - 1
        k += 1
    print()
    i -= 1

# Enter the number of rows: 
# 5
# E D C B A 
#   E D C B 
#     E D C 
#       E D 
#         E
