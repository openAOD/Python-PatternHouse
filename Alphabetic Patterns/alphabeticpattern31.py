alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def triangle(n):
  k = n - 1
  for i in range(0,n):
    for j in range(0,k):
      print(end = " ")
    k -= 1
    for j in range (0, i+1):
      print(alpha[i], end=' ')
    print("") 

print("Enter the number of rows: ")
n = int(input())
triangle(n)

# Enter the number of rows: 
# 5
#     A 
#    B B 
#   C C C 
#  D D D D 
# E E E E E 
