
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Enter the no of rows: ")
n = int(input())
flag = n
for i in range(0, n):
    count = 0
    for j in range(0, n):
        print(alpha[i+count], end=" ")
        if(j%2==0):
            count = count + 2*flag-1
        else:
            count = count + 2*(i+1)-1
    flag = flag -1
    print()
    
# Enter the no of rows: 
# 5
# A J K T U 
# B I L S V 
# C H M R W 
# D G N Q X 
# E F O P Y
