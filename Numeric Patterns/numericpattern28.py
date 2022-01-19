height = int(input())

for i in range(height,0,-1) :

    for j in range(height, i-1,-1):
        print(j,end = " ")
        
    print()

# Sample Input :- 5
# output :-
# 5
# 5 4
# 5 4 3
# 5 4 3 2 
# 5 4 3 2 1

