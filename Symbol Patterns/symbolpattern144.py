height = int(input())
x = 1

for i in range(1,height+1):

    for j in range(1,height+1):

        if((j <= x or j >= height-x+1) and j%2==1):
            print("*",end=" ")
            
        elif((j >= x and j <= height-x+1) and i%2==1):
            print("*",end=" ")
            
        else:
            print(end="  ")

    if(i <= height//2):
        x+=1
        
    else:
        x-=1
        
    print()
    
# Sample Input :- 9
# Output :-
# * * * * * * * * * 
# *               *
# *   * * * * *   *
# *   *       *   *
# *   *   *   *   *
# *   *       *   *
# *   * * * * *   *
# *               *
# * * * * * * * * * 
