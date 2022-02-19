height = int(input()) 

for i in range(1,height+1):

    for j in range(i,height):
        print(end="  ")

    for j in range(i,0,-1):

        if(j%2 == 0):
            print("*",end=" ")

        else:
            print(i,end=" ")

    print()
    
# Sample Input :- 5
# Output :-
#         1 
#       * 2 
#     3 * 3 
#   * 4 * 4 
# 5 * 5 * 5 
