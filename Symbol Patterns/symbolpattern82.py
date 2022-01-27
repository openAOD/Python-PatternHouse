height = int(input())

for i in range(0,height):
        
    for j in range(0,height):
    
        if(i == height-1 or j == 0 or i == j):
            print("*",end=" ")
            
        else:
            print(end="  ")
                
    print()
    
# Sample Input :- 5
# Output :-
# *
# * *
# *   *
# *     *
# * * * * *
