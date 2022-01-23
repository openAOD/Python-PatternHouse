height = int(input())

for i in range(1,height+1):

    for j in range(height,0,-1):
        
        if(i >= j):
            if(j % 2 == 0):
                print("*",end=" ")
            else:
                print(i,end=" ") 
            
        else:
            print(end="  ")
            
    print()
    
# Sample Input :- 5
# Output :-
#         1
#       * 2
#     3 * 3
#   * 4 * 4
# 5 * 5 * 5 
