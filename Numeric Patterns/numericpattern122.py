height = int(input())

for i in range(1,height):

    for j in range(height-i,1,-1):
        print(end="  ")

    for j in range(height-i-1,height-1):
        print(j,end=" ")

    print()

for i in range(1,height):

    for j in range(1,i+1):
        print(end="  ")

    for j in range(height-i,1,-1):
        print(height-j,end=" ")

    print()

# Sample Input :- 5
# Output :-
#       3 
#     2 3 
#   1 2 3 
# 0 1 2 3 
#   1 2 3 
#     2 3 
#       3 
        
