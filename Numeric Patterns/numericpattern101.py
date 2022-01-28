
def pattern(n):
    count = n
    for i in range(n):
        
        for j in range(n - i - 1):
            print(' ', end='')
        for k in range(2 * i + 1):
            print(count, end='')
            
        count = count - 1
        print()
        


print("Enter the number of rows: ")
n = int(input())
pattern(n)


# OUTPUT

# Enter the number of rows: 
# 5
#     5
#    444
#   33333
#  2222222
# 111111111
