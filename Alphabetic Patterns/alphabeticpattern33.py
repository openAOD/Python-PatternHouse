alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def pattern(n):
      k = 2*n -2
      for i in range(n,-1,-1):
           for j in range(k,0,-1):
                print(end=" ")
           k = k +1
           for j in range(0, i+1):
                print(alpha[i], end=" ")
           print("\r")


print("Enter the number of rows: ")
n = int(input())
pattern(n)

# Enter the number of rows: 
# 5
#          E E E E E 
#           D D D D 
#            C C C 
#             B B 
#              A 
