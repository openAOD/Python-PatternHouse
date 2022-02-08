height = int(input())
x = 1

for i in range(1,height+1):

    for j in range(1,height+1):
        
        if((j <= x or j > height-x) and j <= height//2):
            print(i,end=" ")
    
        elif((j <= x or j > height-x) and j > height//2):
            print(i,end=" ")
    
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
# 2 2       2 2 
# 3 3 3   3 3 3 
# 4 4 4 4 4 4 4 
# 5 5 5   5 5 5 
# 6 6       6 6 
# 7           7 
