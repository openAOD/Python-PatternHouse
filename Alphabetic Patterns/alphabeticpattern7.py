def pattern(n):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    countj = 0
    for i in range(0,n):
        counti = 0
        for j in range(0,n):
            flag = counti+countj
            if(flag>25):
                flag = flag - 26
            print(alpha[flag],end=" ")
            counti = counti+5
        print("\r")
        countj=countj+1
            
print("Enter the number of rows: ")
n = int(input())
pattern(n)

#OUTPUT

# Enter the number of rows: 
# 5
# A F K P U 
# B G L Q V 
# C H M R W 
# D I N S X 
# E J O T Y 
