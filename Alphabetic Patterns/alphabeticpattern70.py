alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Enter the no of rows: ")
n = int(input())

flag = 0
count = 0
for i in range(0, n):
    for k in range(0,n):
        if((count)%2==0):
            print("*",end=" ")
        else:
            print(alpha[flag],end=" ")
            flag+=1
        count+=1
    print()
    
# Enter the no of rows: 
# 5
# * A * B * 
# C * D * E 
# * F * G * 
# H * I * J 
# * K * L * 
