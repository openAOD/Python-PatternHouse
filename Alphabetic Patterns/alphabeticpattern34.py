alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def pattern(n):
      k = 2*n -2
      for i in range(n,-1,-1):
           for j in range(k,0,-1):
                print(end=" ")
           k = k +1
           count = i
           for j in range(0, i+1):
                print(alpha[count], end=" ")
                count = count - 1
           print("\r")


print("Enter the number of rows: ")
n = int(input())
pattern(n-1)

# Enter the number of rows: 
# 5
#      E D C B A 
#       D C B A 
#        C B A 
#         B A 
#          A 
