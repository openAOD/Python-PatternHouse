height = int(input())

for i in range(1,height+1):

    for j in range(1,height+1):

        if(i == height - j + 1) :
            print("*",end=" ")

        else :
            print(j,end=" ")

    print()
    
# Sample Input :- 5
# Output :-
# 1 2 3 4 * 
# 1 2 3 * 5 
# 1 2 * 4 5 
# 1 * 3 4 5 
# * 2 3 4 5 
