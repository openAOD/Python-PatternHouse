alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Enter the no of rows: ")
n = int(input())
subAlpha = alpha[0:n]
for i in range(0, n):
    flag = i
    for j in range(0, n):
        if(flag>4):
            flag = flag - 5
        print(subAlpha[flag], end=" ")
        flag+=1
    print()

# Enter the no of rows: 
# 5
# A B C D E 
# B C D E A 
# C D E A B 
# D E A B C 
# E A B C D 
