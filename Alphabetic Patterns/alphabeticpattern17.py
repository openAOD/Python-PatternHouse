row = int(input("Enter number of rows : "))
for i in range (65,65+row):
    # inner loop for jth columns
    for j in range(65+row-1,i-1,-1):
        print(chr(j),end="")
        
    print()