height = 5
counter = 0
for i in range(0,height) :
        for j in range(0,height+1) :
            if ( j == counter or j == height - counter and i <= height // 2 ):
                print("Y",end="")
            else :
                print(end=" ")
        print()
        if (i < height // 2) :
            counter = counter + 1