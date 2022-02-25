height = int(input())

for i in range(1,height+1,2):

    for j in range(1,i+1):
        print(i,end=" ")

    print()

for i in range(height-2,0,-2):

    for j in range(height,height-i,-1):
        print(i,end=" ")

    print()

# Sample Input :- 5
# Output :-
# 1 
# 3 3 3 
# 5 5 5 5 5 
# 3 3 3 
# 1 

