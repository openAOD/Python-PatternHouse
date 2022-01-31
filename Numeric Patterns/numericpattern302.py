height = int(input())
x = 1

for i in range(1,height+1):

    for j in range(1, height-i+1):
    
        print("*",end=" ")
        
    for j in range(1,2*i):
        
        if(j <= i):
            print(x-i+j,end=" ")
        else:
            print(x+i-j,end=" ")
        
    for j in range(1,height-i+1):
        print("*",end=" ")
    
    x += 2

    print()
    
# Sample Input :- 5
# Output :-
# * * * * 1 * * * * 
# * * * 2 3 2 * * *
# * * 3 4 5 4 3 * *
# * 4 5 6 7 6 5 4 *
# 5 6 7 8 9 8 7 6 5
