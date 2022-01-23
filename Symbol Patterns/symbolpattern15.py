height = int(input())

for i in range(height, 0, -1):

    for j in range(1,i+1):
    
        print(j,end=" ")
        
    for j in range(1, height-i+1):
        print("*",end=" ")
        
    print()
    
# Sample Input :- 5
# Output :-
# 1 2 3 4 5
# 1 2 3 4 *
# 1 2 3 * *
# 1 2 * * *
# 1 * * * *
