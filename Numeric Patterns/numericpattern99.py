
def pattern(n):
    
    for i in range(n):
        count = 0
        for j in range(n - i - 1):
            print(' ', end='')
        for k in range(2 * i + 1):
            print(count+1, end='')
            count = count + 1
        print()
        


print("Enter the number of rows: ")
n = int(input())
pattern(n)


# OUTPUT-:
  
# Enter the number of rows: 
# 5
#     1
#    123
#   12345
#  1234567
# 123456789
