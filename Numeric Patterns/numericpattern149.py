height = int(input())

for i in range(1,height+1):

    for j in range(1,i+1):
        print(j,end=" ")

    for j in range(height-i,0,-1):
        print("*",end=" ")

    print()

# Sample Input :- 5
# Output :-
# 1 * * * * 
# 1 2 * * * 
# 1 2 3 * * 
# 1 2 3 4 * 
# 1 2 3 4 5 
