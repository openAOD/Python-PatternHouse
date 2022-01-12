alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Enter the no of rows: ")
n = int(input())
for i in range(0, n):
    nflag = n-i
    for j in range(0, i+1):
        print(nflag, end=" ")
        
    for k in range(0,n-i-1):
        print(alpha[i],end=" ")
    print()
    
# Enter the no of rows: 
# 5
# 5 A A A A 
# 4 4 B B B 
# 3 3 3 C C 
# 2 2 2 2 D 
# 1 1 1 1 1 
