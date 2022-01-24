height = int(input())

for i in range(height,0,-1):

    for j in range(1,height-i+1):
    
        print(end="  ")
    
    for j in range(i,0,-1):
    
        if(j%2 == 0):
            print("*",end=" ")
        
        else:
            print(j,end=" ")
             
    print()
    
# Sample Input :- 5
# Output :-
# 5 * 3 * 1
#   * 3 * 1
#     3 * 1
#       * 1
#         1
