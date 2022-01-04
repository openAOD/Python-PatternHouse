print("Enter the no of rows: ")
a = int(input())
counter = 1
iter = 0
for i in range(0, a):
    for j in range(0, a):
        if iter % 2 == 0:
            if j % 2 == 0:
                print("*", end=" ")
            else:
                print(chr(counter+64), end=" ")
                counter += 1
        else:
            if j % 2 != 0:
                print("*", end=" ")
            else:
                print(chr(counter+64), end=" ")
                counter += 1
    iter += 1
    print()
