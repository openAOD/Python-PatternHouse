height = int(input())

for i in range(1, height + 1):

    for j in range(1, height + 1):

        if(i == j or i == height - j + 1):
            print(height - i + 1,end=" ")

        else:
            print(end="  ")

    print()

# Sample Input :- 5
# Output :-
# 5       5 
#   4   4   
#     3     
#   2   2   
# 1       1 
