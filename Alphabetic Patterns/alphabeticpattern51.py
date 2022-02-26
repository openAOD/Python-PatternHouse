height = int(input())

for i in range(1,height):

    for j in range(height-i,1,-1):
        print(end="  ")

    for j in range(height-i-1,height-1):
        c = chr(j+65)
        print(c,end=" ")

    print()

for i in range(1,height):

    for j in range(1,i+1):
        print(end="  ")

    for j in range(height-i,1,-1):
        c = chr(height-j+65)
        print(c,end=" ")

    print()

# Sample Input :- 5
# Output :-
#       D 
#     C D 
#   B C D 
# A B C D 
#   B C D 
#     C D 
#       D 
        
