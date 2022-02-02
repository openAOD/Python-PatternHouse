height = int(input())
x = height//2+1

for i in range(1,height+1):
    
    for j in range(1,height+1):

        if(i == height//2+1 or j == x):
            print("*",end=" ")
            
        else:
            print(end="  ")

    if(i <= height//2):
        x+=1
    else:
        x-=1
        
    print()
    
# Sample Input :- 7
# Output :-
#      *
#         *
#           *
# * * * * * * *
#           *
#         *
#       *
