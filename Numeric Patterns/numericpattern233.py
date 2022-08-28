for i in range(1,6):
    for j in range(1,6):
        if i==int(5/2)+1 or j==int(5/2)+1:
            print(abs(i-j),end=' ')
        else:
            print(" ",end=' ')
    print(end='\n')
