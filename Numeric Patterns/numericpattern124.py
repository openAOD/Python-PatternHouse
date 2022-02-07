print("Enter the no of rows: ")
n = int(input())
for i in range(n):
    for j in range(n):
        if(i%2==0):
            print(j+1, end=" ")
        else:
            print(n-j, end=" ")
    print()
    
# OUTPUT

# Enter the no of rows: 
# 5
# 1 2 3 4 5 
# 5 4 3 2 1 
# 1 2 3 4 5 
# 5 4 3 2 1 
# 1 2 3 4 5 
