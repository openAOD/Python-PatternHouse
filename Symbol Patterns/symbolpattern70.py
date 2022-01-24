height = int(input())

for i in range(height,-1,-1):

    for j in range(0,i+1):
    
        if(j == i):
            print(i,end="  ")
        
        else:
            print("*",end=" ")
    
    print()
    
# Sample Input :- 5
# Output :-
# * * * * * 5
# * * * * 4
# * * * 3
# * * 2
# * 1
# 0
