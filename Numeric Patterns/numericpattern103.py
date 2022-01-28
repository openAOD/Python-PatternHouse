
def pattern(n):
    
    for i in range(n):
        count = n+i
        for j in range(n - i - 1):
            print(' ', end='')
        for k in range(2 * i + 1):
            print(count, end='')
            count = count - 1
        print()
        


print("Enter the number of rows: ")
n = int(input())
pattern(n)

# Enter the number of rows: 
# 5
#     5
#    654
#   76543
#  8765432
# 987654321
