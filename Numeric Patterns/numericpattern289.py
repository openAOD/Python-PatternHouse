height = int(input())
x = 1

for i in range(1,height+1):

    for j in range(1,height+1):
        
        if((j <= x or j > height-x) and j <= height//2):
            print(j,end=" ")
    
        elif((j <= x or j > height-x) and j > height//2):
            print(height-j+1,end=" ")
    
        else:
            print(end="  ")
            
    if(i <= height//2):
        x += 1
    else :
        x -= 1
        
    print()
    
# Sample Input :- 7
# Output :-
# 1           1 
# 1 2       2 1 
# 1 2 3   3 2 1 
# 1 2 3 4 3 2 1 
# 1 2 3   3 2 1 
# 1 2       2 1 
# 1           1 
