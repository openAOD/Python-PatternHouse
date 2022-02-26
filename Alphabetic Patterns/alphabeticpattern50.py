height = int(input())

for i in range(0,height+1):

    for j in range(0,height-i):
        print(end="  ")

    for j in range(height,height-i-1,-1):
        c = chr(j+65)
        print(c,end=" ")

    print()

for i in range(height,0,-1):

    for j in range(0,height-i+1):
        print(end="  ")

    for j in range(height,height-i,-1):
        c = chr(j+65)
        print(c,end=" ")

    print()

# Sample Input :- 3
# Output :-
#       D 
#     D C 
#   D C B 
# D C B A 
#   D C B 
#     D C 
#       D 
