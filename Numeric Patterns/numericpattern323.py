height = int(input())

for i in range(0,height):

    for j in range(0,height):
    
        if(i == height//2 or j == height-1):
            print("4",end=" ")
        elif(i < height//2 and j == 0):
            print("4",end=" ")
        else:
            print(end="  ")
    print()
    
# Sample Input :- 5
# Output :
# 4       4
# 4       4
# 4 4 4 4 4
#         4
#         4
