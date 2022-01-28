
def pattern(n):
    
    for i in range(n):
        count = i
        for j in range(n - i - 1):
            print(' ', end='')
        flag = 0
        for k in range(2 * i + 1):
            print(count, end='')
            if(flag==1):
                count = count +1 
            if(count!=0 and flag==0):
                count = count - 1
            if(count==0):
                flag=1
            
        print()
        


print("Enter the number of rows: ")
n = int(input())
pattern(n)


# OUTPUT

# Enter the number of rows: 
# 5
#     0
#    101
#   21012
#  3210123
# 432101234
