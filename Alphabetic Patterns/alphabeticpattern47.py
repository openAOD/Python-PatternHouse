height = int(input())

for i in range(1,height):

    for j in range(height-i,height):
        c = chr(j+64)
        print(c,end=" ")
        
    print()


for i in range(height-2,0,-1):

    for j in range(height-i,height):
        c = chr(j+64)
        print(c,end=" ")

    print()

# Sample Input :- 5
# Output :-
# D 
# C D 
# B C D 
# A B C D 
# B C D 
# C D 
# D 
