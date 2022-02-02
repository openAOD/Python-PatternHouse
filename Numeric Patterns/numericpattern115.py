print("Enter the number of rows: ")
n = int(input())
for i in range(n):
    count = 1
    for j in range(0,2*(n-i)-1):
        print(count,end="");
        count+=1
        
    print()
    
# OUTPUT
# Enter the number of rows: 
# 5
# 123456789
# 1234567
# 12345
# 123
# 1
