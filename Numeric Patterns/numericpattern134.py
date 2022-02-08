print("Enter the no of rows: ")
n = int(input())
count = 1
for i in range(n):
    for j in range(n):
        print(count, end=" ")
        count+=1
    if(count>24):
        count-=10
    else:
        count+=5
    
    print()
    
Enter the no of rows: 
5
1 2 3 4 5 
11 12 13 14 15 
21 22 23 24 25 
16 17 18 19 20 
26 27 28 29 30 
