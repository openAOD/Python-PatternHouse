height = int(input())

for i in range(1, height + 1):

    for j in range(1, height + 1):

        if(i == height//2 + 1):
            print(j,end=" ")

        elif(j == height//2 + 1):
            print(height - i + 1,end=" ")

        else:
            print(end="  ")

    print()

# Sample Input :- 5
# Output :-
#     5     
#     4     
# 1 2 3 4 5 
#     2     
#     1     
