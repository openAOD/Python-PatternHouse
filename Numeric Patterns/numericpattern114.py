print("Enter the number of rows: ")
n = int(input())
count = 2*n-1
for i in range(n):
    print(" "*i +  str(count)*(2*(n-i)-1))
    count-=2
    
    
# OUTPUT
    
# print("Enter the number of rows: ")
# n = int(input())
# count = 2*n-1
# for i in range(n):
#     print(" "*i +  str(count)*(2*(n-i)-1))
#     count-=2
