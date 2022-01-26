
def pattern(n):
      k = 2*n -2
      for i in range(n,-1,-1):
           for j in range(k,0,-1):
                print(end=" ")
           k = k +1
           for j in range(0, i+1):
                print(i, end=" ")
           print("")


print("Enter the number of rows: ")
n = int(input())
pattern(n)


OUTPUT

# Enter the number of rows: 
# 5
# 5 5 5 5 5 5 
#  4 4 4 4 4 
#   3 3 3 3 
#    2 2 2 
#     1 1 
#      0
