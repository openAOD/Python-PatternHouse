height = 4
num = 1

for i in range(height,-height-1,-1):
    
    for j in range(1,abs(i)+1):
        print(end="  ")
        
    for j in range(height,abs(i)-1,-1):
        print(height-j+1,end="   ")
            
    if(i > 0):
        num += 1
        
    else: 
        num -= 1
            
    print()

# Output :-
#         1   
#       1   2   
#     1   2   3   
#   1   2   3   4   
# 1   2   3   4   5   
#   1   2   3   4   
#     1   2   3   
#       1   2   
#         1   
