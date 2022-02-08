height = int(input())
x = -height//2+2

for i in range(1,height+1):

    for j in range(1,height+1):
        
        if(j == x or j == height//2+1 or j == height-x+1):
            print("*",end=" ")
            
        else:
            print(end="  ")
        
    x += 1     
    print()
    
# Sample Input :- 7
# Output :-
#       *
#       *
#       *
# *     *     *
#   *   *   *
#     * * *
#       *
