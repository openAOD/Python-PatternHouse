height = int(input())

for i in range(0,height):

    for j in range(i,0,-1):
        print(j,end=" ")

    for j in range(0,height-i):
        print(j,end=" ")

    print()

# Sample Input :- 5
# Output :-
# 0 1 2 3 4 
# 1 0 1 2 3 
# 2 1 0 1 2 
# 3 2 1 0 1 
# 4 3 2 1 0 
