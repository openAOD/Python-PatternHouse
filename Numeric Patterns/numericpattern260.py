height = int(input())
x = 1
c = 1

for i in range(1,height+1):

    for j in range(1,height+1):
    
        if(j == x):
            print(c,end=" ")
            c += 1
        
        else:
            print(end="  ")

        
    if(i <= height//2):
        x += 1
    else:
        x -= 1
        
    print()
    
# Sample Input :- 7
# Output :-
# 1             
#   2           
#     3         
#       4       
#     5         
#   6           
# 7             
