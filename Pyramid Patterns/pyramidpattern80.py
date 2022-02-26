height = int(input())
k = height-1

for i in range(1,height+1):

    for j in range(1,k+1):
        print(end="  ")

    for j in range(1,i*2+1):
        print("*",end=" ")

    k -= 1
    print()

# Sample Input :- 5
# Output :-
#         * * 
#       * * * * 
#     * * * * * * 
#   * * * * * * * * 
# * * * * * * * * * * 
