height = int(input())

for i in range(1, height + 1):

    for j in range(1, height + 1):

        if(i == j):
            print(height - i + 1,end=" ")

        elif(i == height - j + 1):
            print(height - j + 1,end=" ")

        else:
            print(end="  ")

    print()

# Sample Input :- 5
# Output :-
# 5       1 
#   4   2   
#     3     
#   4   2   
# 5       1 
