import math

def pattern(n):
    
    for i in range(n):
        count = 1
        for j in range(n - i - 1):
            print(' ', end='')
        flag = 0
        for k in range(2 * i + 1):
            print(count, end='')
            if(flag==1):
                count = int(count / 2) 
            if(count!=0 and flag==0):
                count = count * 2
            if(count>=(i+1)):
                flag=1
            
        print()
        


print("Enter the number of rows: ")
n = int(input())
pattern(n)


# OUTPUT

# Enter the number of rows: 
# 5
#     1
#    121
#   12421
#  1242100
# 124842100
