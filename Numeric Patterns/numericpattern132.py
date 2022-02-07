print("Enter the no of rows: ")
n = int(input())
count = 0
for i in range(n):
    flag = 0
    for j in range(n):
        print(count+1, end=" ")
    if(count<4):
        count+=2
    else:
        count-=2
    print()
