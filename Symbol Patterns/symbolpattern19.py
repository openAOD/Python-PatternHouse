height = int(input())

for i in range(height, 0, -1):

    for j in range(1, height-i+1):
        
        print("*",end=" ")
        
    for j in range(i,0,-1):
        print(j,end=" ")
            
    print()
    
# Sample Input :- 5
# Output :-
# 5 4 3 2 1
# * 4 3 2 1
# * * 3 2 1
# * * * 2 1
# * * * * 1
