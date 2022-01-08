alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def pattern(n):
      k = 2*n -2
      for i in range(n,-1,-1):
           for j in range(k,0,-1):
                print(end=" ")
           k = k +1
           count = 0
           for j in range(0, i+1):
                print(alpha[count], end=" ")
                count = count + 1
           print("\r")


print("Enter the number of rows: ")
n = int(input())
pattern(n-1)

# Enter the number of rows: 
# 5
#      A B C D E 
#       A B C D 
#        A B C 
#         A B 
#          A 
