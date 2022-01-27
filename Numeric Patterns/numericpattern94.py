def triangle(n):
  k = n - 1
  for i in range(0,n):
    for j in range(0,k):
      print(end = " ")
    k -= 1
    for j in range (0, i+1):
      print(j+1, end=' ')
    print("") 

print("Enter the number of rows: ")
n = int(input())
triangle(n)


OUTPUT

# Enter the number of rows: 
# 5
#     1 
#    1 2 
#   1 2 3 
#  1 2 3 4 
# 1 2 3 4 5 
