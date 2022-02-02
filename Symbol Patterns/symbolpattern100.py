height = int(input())
x = 1

for i in range(1,height+1):

    for j in range(1,x+1):
    
        if(i != height//2+1):
            print("*",end=" ")
        
        else:
            c = chr(j+64)
            print(c,end=" ")
            
    if(i < height//2+1):
        x += 1
    else:
        x -= 1
    
    print()
    
# Sample Input :- 5
# Output :-
# *
# * *
# A B C
# * *
# *
