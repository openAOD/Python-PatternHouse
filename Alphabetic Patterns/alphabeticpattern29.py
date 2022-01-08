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
    k = 1
    while k <= i:
        print(alpha[rows-i], end=' ')
        k += 1
    print()
    i -= 1

# Enter the number of rows: 
# 5
# A A A A A 
#   B B B B 
#     C C C 
#       D D 
#         E 
