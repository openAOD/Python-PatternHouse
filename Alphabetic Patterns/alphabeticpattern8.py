def pattern(n):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    countj = 0
    for i in range(0,n):
        counti = 4
        for j in range(0,n):
            flag = counti+countj
            if(flag>25):
                flag = flag - 26
            print(alpha[flag],end=" ")
            counti = counti+5
        print("\r")
        countj=countj-1
            
print("Enter the number of rows: ")
n = int(input())
pattern(n)


# OUTPUT

# Enter the number of rows: 
# 5
# E J O T Y 
# D I N S X 
# C H M R W 
# B G L Q V 
# A F K P U 
