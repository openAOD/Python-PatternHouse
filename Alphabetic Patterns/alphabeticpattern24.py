num=int(input("Enter Number of Rows:"))
for i in range(65, 64+num+1):
    for j in range(64+num, 64, -1):
        if(j <= i):
            a = chr(j)
            print(a, end="")
        else:
            print(" ", end="")
    print()