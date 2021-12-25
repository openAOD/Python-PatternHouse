height = 5
for i in range(0,height) :
        for j in range(0,height) :
            if ( i == 0 ):
                print("T",end="")
            elif ( j == height // 2 ) :
                print("T",end="")
            else :
                print(end=" ")
        print()