
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Enter the no of rows: ")
n = int(input())
flag = n
wflag = n - 1
for i in range(0, n):
    count = 0
    for j in range(0, n):
        print(alpha[wflag+count], end=" ")
        if(j%2!=0):
            count = count + 2*flag-1
        else:
            count = count + 2*(i+1)-1
    flag = flag -1
    wflag-=1
    print()
    
# Enter the no of rows: 
# 5
# E F O P Y 
# D G N Q X 
# C H M R W 
# B I L S V 
# A J K T U 
