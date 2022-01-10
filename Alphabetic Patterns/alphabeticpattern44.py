print("Enter the number of rows: ")
n = int(input())
count = 2*n-2
for i in range(n):
    print(" "*i + alpha[count]*(2*(n-i)-1))
    count-=2
