
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Enter the no of rows: ")
n = int(input())

for i in range(0, n):
    for k in range(0,i+1):
        print(alpha[i],end=" ")
        
    count = i+1
    for j in range(0,n-i-1):
        print(alpha[count], end=" ")
        count+=1
    print()
    
# Enter the no of rows: 
# 5
# A B C D E 
# B B C D E 
# C C C D E 
# D D D D E 
# E E E E E
