height = int(input())

for i in range(0,height):

    for j in range(0,height):
    
        if(i == height//2 or j == height-1):
            print("*",end=" ")
        elif(i < height//2 and j == 0):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
    
# Sample Input :- 5
# Output :-
# *       *
# *       *
# * * * * *
#         *
#         8
