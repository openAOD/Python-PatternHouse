height = int(input())

for i in range(0,height):

    for j in range(1,height):
    
        if(i == 0 or i == height-j):
            print("*",end=" ")
        else:
            print(end="  ")
            
    print()
    
# Sample Input :- 5
# Output :-
# * * * *
#       *
#     *
#   *
# 8
