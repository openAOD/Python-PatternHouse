alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("Enter the no of rows: ")
n = int(input())

flag = 0

for i in range(0, n):
    count = 0
    for j in range(0,2*(n-i)):
        a = (n-i)
        if(j<a):
            print(alpha[count],end=" ")
            if(count==a-1):
                count=count+0
            else:
                count+=1
        else:
            print(alpha[count],end=" ")
            count-=1
    print()
    
# Enter the no of rows: 
# 5
# A B C D E E D C B A 
# A B C D D C B A 
# A B C C B A 
# A B B A 
# A A
