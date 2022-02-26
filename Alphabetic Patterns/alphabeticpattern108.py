height = int(input())
x = 1

for i in range(1,height+1):

    for j in range(1,x+1):
        if(j == x):
            c = chr(j+64)
            print(c,end=" ")

        else:
            print(end="  ")

    if(i <= height//2):
        x += 1

    else:
        x -= 1

    print()

# Sample Input :- 5
# Output :-
# A 
#   B 
#     C 
#       D 
#     C 
#   B 
# A 
