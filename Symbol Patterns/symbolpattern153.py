height = int(input())

for i in range(1,height+1):
    
    for j in range(height,i,-1):
    
        print(end="  ")
        
    for k in range(1,height):
    
        print("*",end=" ")
        
    print()
    
# Sample Input :- 5
# Output :-
#         * * * *
#       * * * *
#     * * * *
#   * * * *
# * * * *
