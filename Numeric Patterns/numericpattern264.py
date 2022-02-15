height = int(input())
x = height//2+1
num = 1

for i in range(1,height+1):

    for j in range(1,height+1):
    
        if(j == x or j == height-x+1):
            print(num,end=" ")
            
        else:
            print(end="  ")
        
    if(i <= height//2):
        x -= 1
        num += 1
        
    else:
        x += 1
        num -= 1

    print()
    
# Sample Input :- 9
# Output :-
#         1         
#       2   2       
#     3       3     
#   4           4   
# 5               5 
#   4           4   
#     3       3     
#       2   2       
#         1         
