height = int(input())
x = height
y = height

for i in range(1,height+1):
    
    for j in range(1,2*height):

        if(j > x and j < y):
            print(end="  ")
            
        else:
            print("*",end=" ")

    x-=1
    y+=1
    
    print()
    
# Sample Input :- 5
# Output :-
# * * * * * * * * *
# * * * *   * * * *
# * * *       * * *
# * *           * *
# *               *
