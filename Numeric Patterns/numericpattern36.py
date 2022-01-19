height = int(input())
m = 1
n = 2

for i in range(1,height+1) :

    for j in range(1, i+1):

        if(n <= 9):
            print("",n,end = " ")
        else:
            print(n,end = " ")
            
        n += 2
        
    print()

# Sample Input :- 5
# Output :-
#  2
#  4  6
#  8 10 12
# 14 16 18 20
# 22 24 26 28 30

