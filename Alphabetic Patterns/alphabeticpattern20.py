def pattern(n):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counter = n
    for i in range(n,0,-1):
        counteri = counter-1
        for j in range(0,i):
            print(alpha[counteri],end=" ")
            counteri = counteri+1
        print("")
        counter = counter - 1
        
print("Enter the number of rows: ")
n = int(input())
pattern(n)


# OUTPUT

# Enter the number of rows: 
# 5
# E F G H I 
# D E F G 
# C D E 
# B C 
# A
