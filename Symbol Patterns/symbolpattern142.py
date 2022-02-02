height = int(input())

for i in range(1, height+1):

    for j in range(1, height+1):

        if(i == height//2+1 or j == height//2+1 or (i == 1 and j >= height//2+1) or (i == height and j <= height//2+1) or (j == 1 and i <= height//2+1) or (j == height and i >= height//2+1)):
            print("*",end=" ")

        else :
            print(end="  ")

    print()
    
# Sample Input :- 7
# Output :-
# *     * * * *
# *     *
# *     *
# * * * * * * *
#       *     *
#       *     *
# * * * *     *  
