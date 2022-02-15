height = int(input())

for i in range(1, height + 1):

    for j in range(1, i + 1):

        if(i == j):
            print(i - 1,end=" ")

        else:
            print("*",end=" ")

    print()

# Sample Input :- 5
# Output :-
# 0 
# * 1 
# * * 2 
# * * * 3 
# * * * * 4 
# * * * * * 5 
