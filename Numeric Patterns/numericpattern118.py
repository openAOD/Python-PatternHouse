height = int(input())

for i in range(1,height-1):

    for j in range(1,i+1):
        print(j,end=" ")

    print()

for i in range(height-1,0,-1):

    for j in range(height,height-i,-1):
        print(height-j+1,end=" ")

    print()
    
# Sample Input :- 5
# Output :-
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 
