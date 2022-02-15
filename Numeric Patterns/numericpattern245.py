height = int(input())
num = 1

for i in range(1, height + 1):

    for j in range(height,0,-1):
    
        if(i == height or j == height or i == height-j+1):
            print(j,end=" ")
            
        else:
            print(end="  ")
        
    print()
    
# Sample Input :- 5
# Output :- 
# 5         
# 5 4       
# 5   3     
# 5     2   
# 5 4 3 2 1 
