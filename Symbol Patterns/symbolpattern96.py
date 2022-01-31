height = int(input())
number = int(input())

for i in range(1,number+1):

    for j in range(1,i+1):

        for k in range(1,j+1):
        
            print("*",end=" ")

        print()
    
    print()
    
# Sample Input :- 6
#                 3
# Output :-
# *
#
# *
# * * 
# 
# * 
# * *
# * * * 
