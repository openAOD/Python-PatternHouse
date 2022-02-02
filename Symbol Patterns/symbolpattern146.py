height = int(input())
x = height

for i in range(1,height+1):
    
    for j in range(1, 2*height):

        if((j>=x and j<=2*height-x) or j<=height-x+1 or j>=height+x-1):
            print("*",end=" ")

        else:
            print(end="  ")
    x-=1

    print()
    
# Sample Input :- 7
# Output :-
# *           *           *
# * *       * * *       * *
# * * *   * * * * *   * * *
# * * * * * * * * * * * * *   
# * * * * * * * * * * * * *   
# * * * * * * * * * * * * *   
# * * * * * * * * * * * * *   
