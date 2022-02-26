height = int(input())

for i in range(1,height+1):

    for j in range(1,height+1):
        
        if(i < height//2+1):
            print(0,end=" ")

        else:
            print(1,end=" ")

    print()
    
# Sample Input :- 5
# Output :-
# 0 0 0 0 0 
# 0 0 0 0 0 
# 1 1 1 1 1 
# 1 1 1 1 1 
# 1 1 1 1 1 
