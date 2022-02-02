height = int(input())

for i in range(1, height+1):

    for j in range(1, height+1):

        if(j == i or j == height//2+1 or i == height//2+1 or j == height-i+1):
            print("*",end=" ")

        else :
            print(end="  ")

    print()
    
# Sample Input :- 7
# Output :-
# *     *     *
#   *   *   *
#     * * *
# * * * * * * *
#     * * *
#   *   *   *
# *     *     *
