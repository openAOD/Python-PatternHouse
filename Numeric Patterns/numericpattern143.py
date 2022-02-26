height = int(input())

for i in range(1,height+1):

    for j in range(1,i+1):
        print(1,end=" ")

    for j in range(i,height):
        print(0,end=" ")

    print()
    
# Sample Input :- 5
# Output :-
# 1 0 0 0 0 
# 1 1 0 0 0 
# 1 1 1 0 0 
# 1 1 1 1 0 
# 1 1 1 1 1 
