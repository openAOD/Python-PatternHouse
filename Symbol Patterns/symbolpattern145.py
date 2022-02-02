height = int(input())

for i in range(1,height+1):
    
    for j in range(1,height+1):
    
        if((i+j)%2==1):
            print("*",end=" ")
            
        else:
            print(end="  ")
        
    print()
    
# Sample Input :- 7
# Output :-
#   *   *   *
# *   *   *   *
#   *   *   *
# *   *   *   *
#   *   *   *
# *   *   *   *
#   *   *   *
