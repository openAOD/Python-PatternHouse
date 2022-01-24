height = int(input())

for i in range(1,height+1):

    for j in range(1,height+1):
    
        if(i%2 == 0):
            if(j%2 != 0):
                print("X",end=" ")
        
            else:
                print("O",end=" ")
        
        else:
            if(j%2 != 0):
                print("O",end=" ")
            else:
                print("X",end=" ")
        
    print()
    
# Sample Input :- 5
# Output :-
# O X O X 0
# X O X O X
# O X O X 0
# X O X O X
# O X O X 0
