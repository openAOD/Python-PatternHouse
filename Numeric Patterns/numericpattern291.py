height = 3

for i in range(height,-height-1,-1):

    for j in range(abs(i),-1,-1):
        print(j,end=" ")
    
    print()
    
# Output :-
# 3 2 1 0 
# 2 1 0 
# 1 0 
# 0 
# 1 0 
# 2 1 0 
# 3 2 1 0 
