height = int(input())

for i in range(1,height):

    for j in range(1,i+1):
        c = chr(height-j+64)
        print(c,end=" ")
        
    print()


for i in range(height-1,0,-1):

    for j in range(height-1,height-i,-1):
        c = chr(j+64)
        print(c,end=" ")

    print()

# Sample Input :- 5
# Output :-
# D 
# D C 
# D C B 
# D C B A 
# D C B 
# D C 
# D 
