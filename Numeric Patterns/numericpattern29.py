
print("Enter the number of rows:")
n = int(input())
column_count=n
for i in range(0,n):
    row_count = column_count
    for j in range(0,i+1):
        print(row_count,end=" ")
        row_count+=1
    column_count-=1
    print()
    
