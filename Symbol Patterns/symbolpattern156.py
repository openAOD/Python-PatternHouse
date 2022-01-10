print("Enter the number of rows:")
n = int(input())
counter = n
iterations = 0
for i in range(0, n):
    for j in range(0, counter):
        print("*", end=" ")
    iterations = iterations + 1
    if iterations % 2 == 0:
        counter = counter - 2
    print()
