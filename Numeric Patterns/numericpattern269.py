height = int(input())
x = height//2
y = 1
num = 1

for i in range(1,height+1):

    for j in range(1,x+1):
        print(end="  ")

    for j in range(1,y+1):
        print(num,end=" ")

    if(i <= height//2):
        x -= 1
        y += 2
        num += 1

    else:
        x += 1
        y -= 2
        num -= 1

    print()
    
# Sample Input :- 7
# Output :-
#       1 
#     2 2 2 
#   3 3 3 3 3 
# 4 4 4 4 4 4 4 
#   3 3 3 3 3 
#     2 2 2 
#       1 
