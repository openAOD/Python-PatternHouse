height = int(input())

for i in range(1,height+1):
    
    for j in range(1, height+1):

        if(i == height//2 or i == height or j == 1 or j == height and i >= height//2 or (j%2==1 and i<= height//2)):
            print("*",end=" ")

        else:
            print(end="  ")

    print()
    
# Sample Input :- 7
# Output :- 
# *   *   *   *
# *   *   *   *
# * * * * * * * 
# *           *
# *           *
# *           *
# * * * * * * *
