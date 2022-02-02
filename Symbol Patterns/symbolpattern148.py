height = int(input())
x = height//2

for i in range(0,height):
    
    for j in range(0, height):

        if(i+j >= 3*height//2-1 or i+j <= x or i-j >= x or j-i >= x):
            print("*",end=" ")

        else:
            print(end="  ")

    print()
    
# Sample Input :- 9
# Output :-
# * * * * * * * * *
# * * * *   * * * *
# * * *       * * *
# * *           * *
# *               *
# * *           * *
# * * *       * * *
# * * * *   * * * *
# * * * * * * * * *
