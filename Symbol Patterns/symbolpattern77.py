height = int(input())

for i in range(1, height+1):
    
    for j in range(1,height+1):
    
        if(i == height//2+1 or j == height//2+1):
            print("X",end=" ")
            
        else :
            print("O",end=" ")
    
    print()
    
# Sample Input :- 5
# Output :-
# O O X O O
# O O X O O
# X X X X X
# O O X O O
# O O X O O
