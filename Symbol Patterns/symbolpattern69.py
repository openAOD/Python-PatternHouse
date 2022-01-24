height = int(input())

for i in range(0,height+1):

    for j in range(0,i+1):
    
        if(j == i):
            print(i,end="  ")
        
        else:
            print("*",end=" ")
    
    print()
    
# Sample Input :- 5
# Output :-
# 0
# * 1
# * * 2
# * * * 3
# * * * * 4
# * * * * * 5
