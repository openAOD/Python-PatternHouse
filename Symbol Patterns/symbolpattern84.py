height = int(input())

for i in range(1,height+1):
        
    for j in range(1,height+1):
    
        if(i == height or j == height or i == height-j+1):
            print("*",end=" ")
            
        else:
            print(end="  ")
                
    print()
    
# Sample Input :- 5
# Output :-
#         *
#       * *
#     *   *
#   *     *
# * * * * *
