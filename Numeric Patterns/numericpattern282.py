height = int(input())
x = height//2
y = 1

for i in range(1,height+1):

    for j in range(1,height+1):

        if(j <= x or j >= height//2+x):
            print(end="  ")

        else:
            print(y,end=" ")  
            y += 1

    if(i <= height//2):
        x -= 1

    else:
        x += 1

    print()
    
# Sample Input :- 7
# Output :-
#       1 2     
#     3 4       
#   5 6         
# 7 8           
#   9 10         
#     11 12       
#        13 14     
