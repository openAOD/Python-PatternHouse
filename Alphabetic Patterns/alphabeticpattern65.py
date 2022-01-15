alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Enter the no of rows: ")
n = int(input())
counter = n
for i in range(0, n):
    for k in range(0,n-counter):
        print("*",end=" ")
    count = counter-1
    for j in range(0, n-i):
        print(alpha[count], end=" ")
        count-=1
    counter-=1
    print()
    
# Enter the no of rows: 
# 5
# E D C B A 
# * D C B A 
# * * C B A 
# * * * B A 
# * * * * A
