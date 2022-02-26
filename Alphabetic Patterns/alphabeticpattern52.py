height = int(input())
ch = 1

for i in range(1,height+1):

    for j in range(1,height-i+1):
        print(end="  ")

    for j in range(1,i+1):
        c = chr(ch+64)
        print(c,end=" ")
    ch += 1

    print()

for i in range(height-1,0,-1):

    for j in range(1,height-i+1):
        print(end="  ")

    for j in range(1,i+1):
        c = chr(ch+64)
        print(c,end=" ")
    ch += 1

    print()

# Sample Input :- 4
# Output :-
#       A 
#     B B 
#   C C C 
# D D D D 
#   E E E 
#     F F 
#       G 
