height = int(input())

for i in range(1, height + 1):

    for j in range(1, height + 1):

        if(i == j or i == height - j + 1):
            print(j,end=" ")

        else:
            print(end="  ")

    print()

# Sample Input :- 5
# Output :-
# 1       5 
#   2   4   
#     3     
#   2   4   
# 1       5 
