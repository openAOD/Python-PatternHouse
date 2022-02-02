height = int(input())

for i in range(1,height+1):

    for j in range(1,height+1):

        if(j == height or i == 1 or i == height-j+1):
            print("*",end=" ")

        else:
            print(end="  ")

    print()

# Sample Input :- 7
# Output :-
# * * * * * * *
#           * *
#         *   *
#       *     *
#     *       *
#   *         *
# *           *
