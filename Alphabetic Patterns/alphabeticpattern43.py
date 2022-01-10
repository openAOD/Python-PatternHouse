print("Enter the number of rows: ")
n = int(input())
count = n-1
for i in range(n):
    print(" "*i + alpha[count]*(2*(n-i)-1))
    count-=1
