height = int(input())

for i in range(1,height+1):

    for j in range(1,height//2+2):
    
        if(i+j == height//2+2 or i-j == height//2):
            print("*",end=" ")
        
        else:
            print(end="  ")
        
    print()
    
# Sample Input :- 7
# Output :-
#       *
#     *
#   *
# *
#   *
#     *
#       *

