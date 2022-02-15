height = int(input())
x = height//2
y = 1

for i in range(1,height+1):

    for j in range(1,x+1):
        print(end="  ")

    for j in range(1,y+1):
        print(j,end=" ")

    if(i <= height//2):
        x -= 1
        y += 2

    else:
        x += 1
        y -= 2

    print()
    
# Sample Input :- 7
# Output :-
#       1 
#     1 2 3 
#   1 2 3 4 5 
# 1 2 3 4 5 6 7 
#   1 2 3 4 5 
#     1 2 3 
#       1 
