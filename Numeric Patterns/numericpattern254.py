height = int(input())

for i in range(height,0,-1):

    for j in range(1,height+1):
    
        if(i == height or j == height or j == height-i+1):
            print(j,end=" ")
            
        else:
            print(end="  ")
        
    print()
    
# Sample Input :- 5
# Output :-
# 1 2 3 4 5 
#  2     5 
#    3   5 
#      4 5 
#        5 
