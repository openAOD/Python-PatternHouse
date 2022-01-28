
def pattern(n):
    count = 1
    for i in range(n):
        
        for j in range(n - i - 1):
            print(' ', end='')
        for k in range(2 * i + 1):
            print(count, end='')
            count = count + 1
        print()
        


print("Enter the number of rows: ")
n = int(input())
pattern(n)

# OUTPUT


# Enter the number of rows: 
# 5
#     1
#    234
#   56789
#  10111213141516
# 171819202122232425
