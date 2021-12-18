num=int(input("Enter Number of Rows:"))
for i in range(65, 65+num):
    for j in range(75+num, i, -1):
        print(" ", end="")
    for k in range(65, i+1):
        a = chr(k)
        print(a, end=" ")
    print()