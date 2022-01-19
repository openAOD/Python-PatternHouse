height = int(input())
m = 1
n = 1

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
#  1 
#  3  5 
#  7  9 11 
# 13 15 17 19 
# 21 23 25 27 29 

