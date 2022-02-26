height = int(input())

for i in range(1,height):

    for j in range(height-i,height):
        print(j-1,end=" ")

    print()

for i in range(height-2,0,-1):

    for j in range(height-i,height):
        print(j-1,end=" ")

    print()
    
# Sample Input :- 5
# Output :-
# 3 
# 2 3 
# 1 2 3 
# 0 1 2 3 
# 1 2 3 
# 2 3 
# 3 
