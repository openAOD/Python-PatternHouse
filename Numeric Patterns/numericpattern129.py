print("Enter the number of rows: ")
n = int(input())
for i in range(n):
    count = 1
    for j in range(0,n):
        print(count,end="");
        if(j==n-i-1):
            count=i+1
    print()
    
# Enter the number of rows: 
# 5
# 1 1 1 1 1 
# 1 1 1 1 2 
# 1 1 1 3 3 
# 1 1 4 4 4 
# 1 5 5 5 5 
