height = int(input())
x = height

for i in range(1,height+1):

    for j in range(1,2*height+1):
        
        if(j == x or j == 2*height-x+1):
            print("*",end=" ")
            
        else:
            print(end=" ")
            
    if(i % 2 == 0):
        x -= 2
        
    print()
    
# Sample Input :- 7
# Output :-
#       * *
#       * * 
#     *     * 
#     *     *
#   *         *
#   *         * 
# *             *
