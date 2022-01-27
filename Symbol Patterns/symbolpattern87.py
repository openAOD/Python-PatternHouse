height = int(input())
x = 1
y = height*2-1

for i in range(1,height+1):

    for j in range(1,height*2+1):
    
        if(j == x or j == y):
            print("*",end=" ")
        
        else:
            print(end="  ")
        
    x += 1
    y -= 1
        
    print()
    
# Sample Input :- 5
# Output :-
# *               *
#   *           *
#     *       *
#       *   *
#         *
