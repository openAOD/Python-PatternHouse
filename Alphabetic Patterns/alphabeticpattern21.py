def pattern(n):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counter = 0
    for i in range(0,n+1):
        for j in range(0,i):
            if(counter>25):
                counter = counter - 26
            print(alpha[counter],end=" ")
            counter=counter+1
        print("")
        
print("Enter the number of rows: ")
n = int(input())
pattern(n)


# OUTPUT

# Enter the number of rows: 
# 5

# A 
# B C 
# D E F 
# G H I J 
# K L M N O 
