height = int(input()) 

for i in range(height,0,-1):

    for j in range(i,height):
        print(end="  ")

    for j in range(i,0,-1):

        if(i%2 == 0):
            print("*",end=" ")

        else:
            print(j,end=" ")

    print()
    
# Sample Input :- 5
# Output :-
# 5 4 3 2 1 
#   * * * * 
#     3 2 1 
#       * * 
#         1  
