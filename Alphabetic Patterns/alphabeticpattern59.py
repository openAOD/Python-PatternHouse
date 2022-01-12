
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Enter the no of rows: ")
n = int(input())
for i in range(0, n):
    for j in range(0, i+1):
        print(alpha[j], end=" ")
        
    for k in range(0,n-i-1):
        print("*",end=" ")
    print()
    
    
# Enter the no of rows: 
# 5
# A * * * * 
# A B * * * 
# A B C * * 
# A B C D * 
# A B C D E 
