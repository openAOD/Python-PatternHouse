height = int(input())
x = 1

for i in range(1,height+1):

    for j in range(1,i):
        print("*",end=" ")

    for j in range(height-i+1,0,-1):
        print(j,end=" ")

    print()

# Sample Input :- 5
# Output :-
# 5 4 3 2 1 
# * 4 3 2 1 
# * * 3 2 1 
# * * * 2 1 
# * * * * 1 
