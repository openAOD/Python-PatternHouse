height = int(input())

for i in range(1,height+1):

    for j in range(1,height+1):
    
        if(i > j):
            print("X",end=" ")
        
        else:
            print("O",end=" ")
        
    print()
    
# Sample Input :- 5
# Output :-
# O O O O O
# X O O O O
# X X O O O
# X X X O O
# X X X X O
