height = int(input())

for i in range(0,height):

    for j in range(0,i):
        print(0,end=" ")

    for j in range(1,height-i+1):
        print((2*i)+j,end=" ")

    print()
    
# Sample Input :- 5
# Output :-
# 1 2 3 4 5 
# 0 3 4 5 6 
# 0 0 5 6 7 
# 0 0 0 7 8 
# 0 0 0 0 9 
