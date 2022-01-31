height = int(input())
x = 1

for i in range(1,height+1):

    for j in range(1, 2*height):
    
        if(j >= height-i+1 and j <= height+i-1):
            
            print("*",end=" ")
        
        elif(j <= height):
        
            print(j,end=" ")
            
        else:
            print(2*height-j,end=" ")
    print()
    
# Sample Input :- 5
# Output :-
# 1 2 3 4 * 4 3 2 1
# 1 2 3 * * * 3 2 1
# 1 2 * * * * * 2 1
# 1 * * * * * * * 1
# * * * * * * * * *
