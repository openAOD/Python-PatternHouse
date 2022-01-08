alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def pattern(n):
    count = 0
    for i in range(n):
        for j in range(n - i - 1):
            print(' ', end='')
        for k in range(2 * i + 1):
            print(alpha[count], end='')
        print()
        count = count + 1


print("Enter the number of rows: ")
n = int(input())
pattern(n)

# Enter the number of rows: 
# 5
#     A
#    BBB
#   CCCCC
#  DDDDDDD
# EEEEEEEEE
