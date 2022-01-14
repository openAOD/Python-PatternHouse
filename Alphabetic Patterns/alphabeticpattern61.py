
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Enter the no of rows: ")
n = int(input())
for i in range(0, n):
    count = 0
    for k in range(0,n-i):
        print(alpha[count],end=" ")
        count+=1
    for j in range(0, i):
        print("*", end=" ")
    print()
    
# Enter the no of rows: 
# 5
# A B C D E 
# A B C D * 
# A B C * * 
# A B * * * 
# A * * * *
