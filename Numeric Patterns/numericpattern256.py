height = int(input())

for i in range(1,height+1):

    for j in range(1,2*height):
    
        if(j == height+i-1 or j == height-i+1):
            print(i,end=" ")
            
        else:
            print(end="  ")
        
    print()
    
# Sample Input :- 5
# Output :-
#         1         
#       2   2       
#     3       3     
#   4           4   
# 5               5 
