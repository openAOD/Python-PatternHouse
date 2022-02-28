num = int(input("Enter the Number: "))

for i in range(1, num+1):
    for j in range(0, i):
        print(" ", end="")

    for j in range(1, (num*2 - (2*i - 1))+1):
        if i == 1 or j == 1 or j ==(num*2 -(2*i-1)):
            print("*", end="")
        else:
            print(" ", end="")
    print() 