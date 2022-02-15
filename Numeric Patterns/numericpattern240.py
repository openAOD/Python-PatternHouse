height = int(input())

for i in range(1, height + 1):

    for j in range(1, height + 1):
    
        if(i == 1 or i == height or j == 1 or j == height or i == j or i == height - j + 1):
            print(1,end=" ")
    
        else:
            print(end="  ")
        
    print()

# Sample Input :- 5
# Output :-
# 1 1 1 1 1 
# 1 1   1 1 
# 1   1   1 
# 1 1   1 1 
# 1 1 1 1 1 
