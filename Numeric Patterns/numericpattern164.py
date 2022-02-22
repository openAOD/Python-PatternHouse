
height = int(input())

for i in range(1,height+1):
    
    if(i%2 == 0):

        for j in range(i,0,-1):
            print(j,end=" ")

    else:
        for j in range(1,i+1):
            print(j,end=" ")
            
    print()

# Sample Input :- 5
# Output :-
# 1 
# 2 1 
# 1 2 3 
# 4 3 2 1 
# 1 2 3 4 5 
