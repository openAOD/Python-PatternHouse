# Print Pascal's Triangle in Python
from math import factorial
 
# input n
print("Enter the number of rows-: ")
n = int(input())
for i in range(n):
    for j in range(n-i):
 
        # for left spacing
        print(end=" ")
 
    for j in range(i+1):
 
        # nCr = n!/((n-r)!*r!)
        print(factorial(i)//(factorial(j)*factorial(i-j)), end="")
 
    # for new line
    print()
    
#OUTPUT
# Enter the number of rows-: 
# 5
#      1
#     11
#    121
#   1331
#  14641
