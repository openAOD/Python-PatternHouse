
print("Enter the number of rows:")
n = int(input())
count = 17
for i in range(0,n):
    for j in range(0,n-i):
        print(count,end=" ")
        count+=1
    print()
    
