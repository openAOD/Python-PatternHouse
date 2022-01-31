height = int(input())
x = height

for i in range(1,height+1):

    for j in range(1, x+1):
    
        if(i <= height/2+1):
            
            print(j+i-1,end=" ")
        
        else:
            print(j+i-x,end=" ")
            
    if(i <= height/2):
        x -= 2
    else:
        x +=2
        
    print()
    
# Sample Input :- 5
# Output :-
# 1 2 3 4 5 
# 2 3 4
# 3
# 2 3 4
# 1 2 3 4 5
