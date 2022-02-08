height = int(input())
x = height//2+1
num = 1

for i in range(1,height+1):

    for j in range(1,x+1):
        if(num <= 9):
            print("",num,end=" ")
        else:
            print(num,end=" ")
        num += 1
        
    if(i <= height//2):
        x -= 1

    else:
        x += 1

    print()
    
# Sample Input :- 7
# Output :-
#  1  2  3  4 
#  5  6  7 
#  8  9 
# 10 
# 11 12 
# 13 14 15 
# 16 17 18 19 
