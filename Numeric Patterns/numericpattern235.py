height = int(input())

for i in range(1, height + 1):

    for j in range(1, height + 1):
    
        if(i == j or i == height - j + 1):
            print(1,end=" ")
    
        else:
            print(0,end=" ")
        
    print()

# Sample Input :- 5
# Output :- 
# 1 0 0 0 1 
# 0 1 0 1 0 
# 0 0 1 0 0 
# 0 1 0 1 0 
# 1 0 0 0 1 
