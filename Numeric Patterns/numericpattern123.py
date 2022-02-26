height = int(input())
c = 1

for i in range(1,height):

    for j in range(height-i,1,-1):
        print(end="  ")

    for j in range(height-i,height):
        print(c,end=" ")

    c += 1
    print()

for i in range(1,height):

    for j in range(1,i+1):
        print(end="  ")

    for j in range(height-i,1,-1):
        print(c,end=" ")

    c += 1
    print()

# Sample Input :- 5
# Output :-
#       1 
#     2 2 
#   3 3 3 
# 4 4 4 4 
#   5 5 5 
#     6 6 
#       7 
        
