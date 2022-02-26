height = int(input())
ch = 1

for i in range(1,height):

    for j in range(1,i+1):
        c = chr(ch+64)
        print(c,end=" ")
    ch += 1

    print()

for i in range(height-1,1,-1):

    for j in range(height-i+1,height):
        c = chr(ch+64)
        print(c,end=" ")
    ch += 1

    print()

# Sample Input :- 5
# Output :-
# A 
# B B 
# C C C 
# D D D D 
# E E E 
# F F 
# G 
