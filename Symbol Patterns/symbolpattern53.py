height = int(input())

for i in range(height,0,-1):

    for j in range(1,height+1):
        
        if(i <= j):
            if(i % 2 == 0):
                print("*",end=" ")
            else:
                print(j,end=" ") 
            
        else:
            print(end="  ")
            
    print()
    
# Sample Input :- 5
# Output :-
#         5
#       * *
#     3 4 5
#   * * * *
# 1 2 3 4 5
