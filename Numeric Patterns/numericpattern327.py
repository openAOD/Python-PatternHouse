height = int(input())

for i in range(0,height):

    for j in range(0,height):
    
        if(i == 0 or i == height//2 or i == height-1 or j == 0 or j == height-1):
            print("8",end=" ")
        else:
            print(end="  ")
    print()
    
# Sample Input :- 5
# 8 8 8 8 8
# 8       8
# 8 8 8 8 8
# 8       8
# 8 8 8 8 8
