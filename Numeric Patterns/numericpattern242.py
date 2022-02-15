height = int(input())

for i in range(1, height + 1):

    for j in range(1,i+1):
    
        if(i == height or j == 1 or i == j):
            print(j,end=" ")
    
        else:
            print(end="  ")
        
    print()

# Sample Input :- 5
# Output :-
# 1 
# 1 2 
# 1   3 
# 1     4 
# 1 2 3 4 5 
