print("Enter the no of rows: ")
n = int(input())
for i in range(n):
    count = 0
    flag = 0
    for j in range(n):
        if(i==j):
            flag = 1
        if(flag==1):
            print(n-count, end=" ")
            count+=1
        if(flag!=1):
            print("1",end=" ")
    print()
    
# Enter the no of rows: 
# 5
# 5 4 3 2 1 
# 1 5 4 3 2 
# 1 1 5 4 3 
# 1 1 1 5 4 
# 1 1 1 1 5 
