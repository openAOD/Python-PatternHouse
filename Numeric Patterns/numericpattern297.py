height = int(input())

for i in range(1,height+1):

    for j in range(1, height*2+1):
    
        if(j <= i):
            
            print(j,end=" ")
        
        elif(j > height*2-i):
        
            print(height*2-j+1,end=" ")
            
        else:
        
            print(end="  ")
            
    
    print()
    
# Sample Input :- 5
# Output :-
# 1                 1
# 1 2             2 1
# 1 2 3         3 2 1
# 1 2 3 4     4 3 2 1 
# 1 2 3 4 5 5 4 3 2 1
