height = int(input())

for i in range(height, 0, -1):

    for j in range(1, height-i+1):
        
        print("*",end=" ")
        
    for j in range(1,i+1):
        print(i,end=" ")
            
    print()
    
# Sample Input :- 5
# Output :-
# 5 5 5 5 5 
# * 4 4 4 4
# * * 3 3 3
# * * * 2 2
# * * * * 1
