height = 4
num = 1

for i in range(height,-height-1,-1):
    
    for j in range(1,abs(i)+1):
        print(end="  ")
        
    for j in range(height,abs(i)-1,-1):
        print(num,end="   ")
            
    if(i > 0):
        num += 1
        
    else: 
        num -= 1
            
    print()

# Sample Input :- 5
# Output :-
#         1   
#       2   2   
#     3   3   3   
#   4   4   4   4   
# 5   5   5   5   5   
#   4   4   4   4   
#     3   3   3   
#       2   2   
#         1   
