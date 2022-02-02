height = int(input())

for i in range(1,height+1):
    
    for j in range(1,2*height):

        if(j <= i or j >= height*2-i):
            print("*",end=" ")
            
        else:
            print(end="  ")

    print()
    
# Sample Input :- 5
# Output :- 
# *               *
# * *           * *
# * * *       * * *
# * * * *   * * * *
# * * * * * * * * *
