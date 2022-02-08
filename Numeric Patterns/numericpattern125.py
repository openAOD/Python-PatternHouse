
print("Enter the no of rows: ")
n = int(input())
flag = n
for i in range(0, n):
    count = 0
    for j in range(0, n):
        print(i+count+1, end=" ")
        if(j%2==0):
            count = count + 2*flag-1
        else:
            count = count + 2*(i+1)-1
    flag = flag -1
    print()
    
    
# Enter the no of rows: 
# 5
# 1 10 11 20 21 
# 2 9 12 19 22 
# 3 8 13 18 23 
# 4 7 14 17 24 
# 5 6 15 16 25 
