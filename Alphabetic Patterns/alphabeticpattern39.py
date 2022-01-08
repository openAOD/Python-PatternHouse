alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def pattern(n):
    count = 0
    for i in range(n):
        for j in range(n - i - 1):
            print(' ', end='')
        flag = 0
        for k in range(2 * i + 1):
            print(alpha[count+flag], end='')
            flag=flag-1
        print()
        count = count + 2


print("Enter the number of rows: ")
n = int(input())
pattern(n)


# Enter the number of rows: 
# 5
#     A
#    CBA
#   EDCBA
#  GFEDCBA
# IHGFEDCBA
