def pattern(n):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counter = n
    for i in range(n,0,-1):
        counteri = counter-1
        for j in range(0,i):
            print(alpha[counteri],end=" ")
            counteri = counteri-1
        print("")
        counter = counter + 1
        
print("Enter the number of rows: ")
n = int(input())
pattern(n)


# OUTPUT

# Enter the number of rows: 
# 5
# E D C B A 
# F E D C 
# G F E 
# H G 
# I 
