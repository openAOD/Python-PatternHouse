height = int(input())

for i in range(1,height+1):

    for j in range(0,i+1):
        print(end="  ")

    for j in range(i,(2*height)-i+1):
        print(j,end=" ")

    print()

for i in range(1,height):

    for j in range(0,height-i+1):
        print(end="  ")

    for j in range(height-i,height+i+1):
        print(j,end=" ")

    print()
    
# Sample Input :- 4
# Output :-
# 1 2 3 4 5 6 7 
#   2 3 4 5 6 
#     3 4 5 
#       4 
#     3 4 5 
#   2 3 4 5 6 
# 1 2 3 4 5 6 7 
