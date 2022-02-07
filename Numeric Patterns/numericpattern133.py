print("Enter the no of rows: ")
n = int(input())
count = 0
for i in range(n):
    for j in range(n):
        print(count+1, end=" ")
        if(count==7):
           count=-1
        count+=1
    
    print()
    
    
    
# Enter the no of rows: 
# 5
# 1 2 3 4 5 
# 6 7 8 1 2 
# 3 4 5 6 7 
# 8 1 2 3 4 
# 5 6 7 8 1 
