for i in range(1,6):
    for j in range(1,6):
        if i==int(5/2)+1 or j==int(5/2)+1:
            if abs(i-j)==2:
                print(1,end=' ')
            elif abs(i-j)==1:
                print(2,end=' ')
            else:
                print(3,end=' ')
        else:
            print(" ",end=' ')
    print(end='\n')
