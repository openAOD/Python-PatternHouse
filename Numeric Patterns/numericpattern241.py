height = int(input())

for i in range(1, height + 1):

    for j in range(1,i+1):
    
        if(i == height or j == 1 or i == j):
            print(i,end=" ")
    
        else:
            print(end="  ")
        
    print()

# Sample Input :- 5
# Output :-
# 1 
# 2 2 
# 3   3 
# 4     4 
# 5 5 5 5 5 
