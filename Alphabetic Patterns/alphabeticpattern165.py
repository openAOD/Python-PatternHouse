height = 5
counter = height - 1
for i in range(0, height):
     for j in range(0, height):
            if (i == 0 or i == height - 1 or j == counter):
                print("*", end="")
            else:
                print(end=" ")
     counter = counter - 1
     print()
