
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Enter the no of rows: ")
n = int(input())

for i in range(0, n):
    counter = 0
    for k in range(0,n-i):
        print(alpha[counter],end=" ")
        counter+=1
    for j in range(0,i):
        print(alpha[n-i-1], end=" ")
    print()
    
# Enter the no of rows: 
# 5
# A B C D E 
# A B C D D 
# A B C C C 
# A B B B B 
# A A A A A 
