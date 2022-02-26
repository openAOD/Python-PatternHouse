height = int(input())
x = height//2+1

for i in range(1,height+1):

    for j in range(1,x+1):
        if(j == x):
            c = chr(i+64)
            print(c,end=" ")

        else:
            print(end="  ")

    if(i <= height//2):
        x -= 1

    else:
        x += 1

    print()

# Sample Input :- 5
# Output :-
#       A 
#     B 
#   C 
# D 
#   E 
#     F 
#       G 
