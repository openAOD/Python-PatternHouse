height = int(input())
m = 1

for i in range(1,height+1) :

    for j in range(1, i+1):
        
        if(m <= 9):
            print("",m,end = " ")
        else:
            print(m,end = " ")
        m+=1
        
    print()

# Sample Input :- 5
# Output :- 
#  1
#  2  3 
#  4  5  6
#  7  8  9 10
# 11 12 13 14 15
