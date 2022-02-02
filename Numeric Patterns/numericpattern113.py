print("Enter the number of rows: ")
n = int(input())
count = n
for i in range(n):
    print(" "*i +  str(count)*(2*(n-i)-1))
    count-=1
    
# OUTPUT    
# Enter the number of rows: 
# 5
# 555555555
#  4444444
#   33333
#    222
#     1
