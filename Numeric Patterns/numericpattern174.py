height = int(input())

for i in range(height,0,-1):

    for j in range(1,i+1):

        if(i%2 == 1):
            print(j,end=" ")

        else:
            print(i+1-j,end=" ")
            
    print()
            
# Sample Input :- 5
# Output :-
# 1 2 3 4 5 
# 4 3 2 1 
# 1 2 3 
# 2 1 
# 1 
