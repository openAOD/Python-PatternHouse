height = int(input())

for i in range(1,height+1):

    for j in range(1,height-i+2):
        print(j,end=" ")

    for j in range(1,i):
        print("*",end=" ")

    print()

# Sample Input :- 5
# Output :-
# 1 2 3 4 5 
# 1 2 3 4 * 
# 1 2 3 * * 
# 1 2 * * * 
# 1 * * * * 
