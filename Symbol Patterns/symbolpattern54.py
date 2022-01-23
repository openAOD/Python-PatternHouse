height = int(input())

for i in range(1,height+1):

    for j in range(height,0,-1):
        
        if(i >= j):
            if(j % 2 == 0):
                print("*",end=" ")
            else:
                print(j,end=" ") 
            
        else:
            print(end="  ")
            
    print()
    
# Sample Input :- 5
# Output :-
#         1
#       * 1
#     3 * 1
#   * 3 * 1
# 5 * 3 * 1
