height = int(input())

for i in range(1,height+1):

    for j in range(1,i+1):
        print(height-i+1,end=" ")

    for j in range(i,height):
        c = chr(i+64)
        print(c,end=" ")

    print()
    
# Sample Input :- 5
# Output :-
# 5 A A A A 
# 4 4 B B B 
# 3 3 3 C C 
# 2 2 2 2 D 
# 1 1 1 1 1 
