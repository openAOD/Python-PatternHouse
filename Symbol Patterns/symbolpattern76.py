height = int(input())

for i in range(1, height+1):
    
    for j in range(1,height+1):
    
        if(i == height//2+1 and j == height//2+1):
            print("O",end=" ")
            
        else :
            print("X",end=" ")
    
    print()
    
# Sample Input :- 5
# Output :- 
# X X X X X
# X X X X X
# X X O X X
# X X X X X
# X X X X X
