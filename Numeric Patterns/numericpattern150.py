height = int(input())

for i in range(1,height+1):

    for j in range(1,height-i+2):
        print(height-i+1,end=" ")

    for j in range(1,i):
        print("*",end=" ")

    print()


# Sample Input :- 5
# Output :-
# 5 5 5 5 5 
# 4 4 4 4 * 
# 3 3 3 * * 
# 2 2 * * * 
# 1 * * * * 
