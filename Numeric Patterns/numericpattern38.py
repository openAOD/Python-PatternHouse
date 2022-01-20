
print("Enter the number of rows:")
n = int(input())
column_count=0
for i in range(0,n):
    row_count = column_count+1
    for j in range(0,i+1):
        print(row_count,end=" ")
        row_count=row_count-(n-j-i)
    column_count=column_count+n-i
    print()
    
