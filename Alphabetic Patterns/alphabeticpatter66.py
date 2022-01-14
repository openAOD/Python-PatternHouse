alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Enter the no of rows: ")
n = int(input())

for i in range(0, n):
    counter = 0
    for k in range(0,i+1):
        print(alpha[counter],end=" ")
        counter+=1
    for j in range(0, n-(i+1)):
        print(alpha[i], end=" ")
    print()
    
# Enter the no of rows: 
# 5
# A A A A A 
# A B B B B 
# A B C C C 
# A B C D D 
# A B C D E
