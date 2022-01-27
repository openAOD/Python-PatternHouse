height = int(input())

for i in range(0,height):
   
    for j in range(0,height):

        if(i == j):
            print("O",end=" ")

        else :
            print("X",end=" ")

    print()
    
# Sample Input :- 5
# Output :-
# O X X X X
# X O X X X
# X X O X X 
# X X X O X
# X X X X O
