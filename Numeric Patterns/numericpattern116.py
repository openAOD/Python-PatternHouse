height = int(input())

for i in range(1,height):

    for j in range(1,i+1):
        print(height-j-1,end=" ")

    print()

for i in range(height-1,0,-1):

    for j in range(height-1,height-i,-1):
        print(j-1,end=" ")

    print()
    
# Sample Input :- 5
# Output :-
# 3 
# 3 2 
# 3 2 1 
# 3 2 1 0 
# 3 2 1 
# 3 2 
# 3 
