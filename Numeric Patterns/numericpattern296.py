height = int(input())
x = 1

for i in range(1,height+1):

    for j in range(1,height//2+2):
    
        if(j >= x):
            print(j,end=" ")
        else:
            print(end="  ")
        
    if(i <= height//2):
        x += 1

    else:
        x -= 1

    print()
    
# Sample Input :- 7
# Output :-
# 1 2 3 4
#   2 3 4
#     3 4
#       4
#     3 4
#   2 3 4
# 1 2 3 4
