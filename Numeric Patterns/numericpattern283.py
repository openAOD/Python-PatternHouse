height = int(input())
x = 1

for i in range(1,height+1):

    for j in range(1,x+1):
    
        if(i != height//2+1):
            print("*",end=" ")
        
        else:
            print(j,end=" ")
            
    if(i < height//2+1):
        x += 1
    else:
        x -= 1
    
    print()
    
# Sample Input :- 5
# Output :-
# *
# * *
# 1 2 3
# * *
# *
