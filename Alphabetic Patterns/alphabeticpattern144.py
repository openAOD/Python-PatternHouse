height = 5
for i in range(0,height) :
        print("*",end="")
        for j in range(0,height) :
            if ( (i == 0 or i == height - 1) or (i == height // 2 and j <= height // 2) ):
                print("*",end="")
            else :
                continue
        print()