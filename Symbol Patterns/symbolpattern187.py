height = 5
width = 2*height-1
for i in range(0, height):
       for j in range(0, width-1):
            if ((i == 0 or i == height - 1) and (j == 0 or j == width - 2)):
                print(end=" ")
            elif (j == 0):
                print("*", end="")
            elif (i == 0 and j <= height):
                print("*", end="")
            elif (i == height // 2 and j > height // 2):
                print("*", end="")
            elif (i > height // 2 and j == width - 2):
                print("*", end="")
            elif (i == height - 1 and j < width - 1):
                print("*", end="")
            else:
                print(end=" ")
       print()
