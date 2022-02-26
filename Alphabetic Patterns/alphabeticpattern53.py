height = int(input())

for i in range(1,height+1):

    for j in range(1,height-i+1):
        print(end="  ")

    for j in range(1,i+1):
        c = chr(j+64)
        print(c,end=" ")

    print()

for i in range(height-1,0,-1):

    for j in range(1,height-i+1):
        print(end="  ")

    for j in range(1,i+1):
        c = chr(j+64)
        print(c,end=" ")

    print()

# Sample Input :- 5
# Output :-
#       A 
#     A B 
#   A B C 
# A B C D 
#   A B C 
#     A B 
#       A 
