
print("Enter the number of rows:")
n = int(input())
count = n
flag = n
for i in range(0,n):
    minus = n-1
    count=flag
    for j in range(0,n-i):
        print(count,end=" ")
        count+=minus
        minus=minus-1
    flag=flag-1
    print()
