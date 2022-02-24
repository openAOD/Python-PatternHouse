height = 3

for i in range(height,-height-1,-1):

    for j in range(0,abs(i)+1):
        print(j,end=" ")
    
    print()
    
# Output :-
# 0 1 2 3 
# 0 1 2 
# 0 1 
# 0 
# 0 1 
# 0 1 2 
# 0 1 2 3 
