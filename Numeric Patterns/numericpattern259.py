height = int(input())

for i in range(height,0,-1):

    for j in range(1,2*height):
    
        if(j == height+i-1 or j == height-i+1):
            print(i,end=" ")
            
        else:
            print(end="  ")
        
    print()
    
# Sample Input :- 5
# Output :-
# 5               5 
#   4           4   
#     3       3     
#       2   2       
#         1         
