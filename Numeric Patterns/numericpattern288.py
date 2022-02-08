height = int(input())
x = 1

for i in range(1,height+1):

    for j in range(1,height+1):
        
        if((j <= x or j > height-x) and j <= height//2):
            print(j,end=" ")
    
        elif((j <= x or j > height-x) and j > height//2):
            print(j,end=" ")
    
        else:
            print(end="  ")
            
    if(i <= height//2):
        x += 1
    else :
        x -= 1
        
    print()
    
# Sample Input :- 7
# Output :-
# 1           7 
# 1 2       6 7 
# 1 2 3   5 6 7 
# 1 2 3 4 5 6 7 
# 1 2 3   5 6 7 
# 1 2       6 7 
# 1           7 
