height = 5
for i in range(0,height) :
        for j in range(0,height) :
            if(i==0):
                 print("*",end="")
            if ( i == height - 1 and (j > 0 and j < height - 1) ):
                print("*",end="")
            elif ( (j == height - 1 and i != height - 1) or (i > (height // 2) - 1 and j == 0 and i != height - 1) ) :
                print("*",end="")
            else :
                print(end=" ")
        print()