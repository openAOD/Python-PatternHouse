height = int(input())

for i in range(1,height+1):

    for j in range(1,height+1):

        if(j == 1 or i == height or i == j):
            print("*",end=" ")

        elif(i == height-j+1 and i <= height//2 and j >= height//2):
            print("*",end=" ")
            
        else:
            print(end="  ")

    print()
    
# Sample Input :- 7
# Output :-
# *           *
# * *       *
# *   *   *
# *     *
# *       *
# *         *
# * * * * * * * 
