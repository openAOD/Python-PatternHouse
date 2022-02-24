height = int(input())

for i in range(1,height+1):

    for j in range(1,height-i+1):
        print("*",end=" ")

    for j in range(i,0,-1):
        print(i,end=" ")

    print()

# Sample Input :- 5
# Output :-
# * * * * 1 
# * * * 2 2 
# * * 3 3 3 
# * 4 4 4 4 
# 5 5 5 5 5 
