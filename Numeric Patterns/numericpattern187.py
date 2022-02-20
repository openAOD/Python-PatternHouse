height = int(input()) 

for i in range(1,height+1):

    for j in range(0,height-i):
        print(end="  ")

    for j in range(i,0,-1):

        if(i%2 == 0):
            print("*",end=" ")

        else:
            print(i,end=" ")

    print()
    
# Sample Input :- 5
# Output :-
#         1 
#       * * 
#     3 3 3 
#   * * * * 
# 5 5 5 5 5 
