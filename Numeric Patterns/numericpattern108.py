import math

def pattern(n):
    
    for i in range(n):
        count= i+1
        for j in range(n - i - 1):
            print(' ', end='')
        flag = 0
        for k in range(2 * i + 1):
            print(count, end='')
            if(flag==1):
                count = count+1 
            if(count!=0 and flag==0):
                count = count - 1
            if(count==1):
                flag=1
            
        print()
        


print("Enter the number of rows: ")
n = int(input())
pattern(n)

# OUTPUT

# Enter the number of rows: 
# 5
# 1
#    212
#   32123
#  4321234
# 543212345
