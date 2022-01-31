height = int(input())
x = height+1

for i in range(1,height+1):

    for j in range(1, x+1):
    
        if(j <= x/2):
            
            print(j,end=" ")
        
        else:
            print(x-j+1,end=" ")
            
    if(i <= height/2):
        x -= 2
    else:
        x +=2
        
    print()
    
# Sample Input :- 5
# Output :-
# 1 2 3 3 2 1
# 1 2 2 1
# 1 1
# 1 2 2 1
# 1 2 3 3 2 1
