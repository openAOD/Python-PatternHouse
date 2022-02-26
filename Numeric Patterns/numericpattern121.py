height = int(input())

for i in range(0,height+1):

    for j in range(0,height-i):
        print(end="  ")

    for j in range(height,height-i-1,-1):
        print(j,end=" ")

    print()

for i in range(height,0,-1):

    for j in range(0,height-i+1):
        print(end="  ")

    for j in range(height,height-i,-1):
        print(j,end=" ")

    print()

# Sample Input :- 3
# Output :-
#       3 
#     3 2 
#   3 2 1 
# 3 2 1 0 
#   3 2 1 
#     3 2 
#       3 
