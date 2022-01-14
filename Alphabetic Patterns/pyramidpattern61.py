alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Enter the no of rows: ")
n = int(input())

for i in range(0, n):
    for k in range(0,n-i):
        print(alpha[n-i-1],end=" ")
        
    count = n-i
    for j in range(0,i):
        print(alpha[count], end=" ")
        count+=1
    print()
    
    
# Enter the no of rows: 
# 5
# E E E E E 
# D D D D E 
# C C C D E 
# B B C D E 
# A B C D E
