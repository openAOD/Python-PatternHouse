print("Enter the number of rows: ")
n = int(input())
n = int(n/2)
spaces = n + (n - 1)
counter = 1
count = 0
for i in range(0, n):
    for i in range(2):
        for k in range(0, spaces):
            print(" ", end="")
        for j in range(0, counter):
            print("*", end=" ")
        print()
    counter = counter + 2
    spaces = spaces - 2
    
# EXAMPLE OUTPUT

# Enter the number of rows: 
# 6
#      * 
#      * 
#    * * * 
#    * * * 
#  * * * * * 
#  * * * * * 
