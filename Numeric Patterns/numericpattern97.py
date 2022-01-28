
def pattern(n):
    count = 0
    for i in range(n):
        for j in range(n - i - 1):
            print(' ', end='')
        for k in range(2 * i + 1):
            print(count+1, end='')
        print()
        count = count + 1


print("Enter the number of rows: ")
n = int(input())
pattern(n)


# OUTPUT

# Enter the number of rows: 
# 5
#     1
#    222
#   33333
#  4444444
# 555555555
