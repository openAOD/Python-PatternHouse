height = int(input())

for i in range(0,height+1):

    for j in range(0,i):
        print(end=" ")

    for j in range(height,i,-1):
        
        if(i%2 == 0):
            print("#",end=" ")

        else:
            print("*",end=" ")

    print()
    
# Sample Input :- 5
# Output :-
# # # # # # 
#  * * * * 
#   # # # 
#    * * 
#     # 
     
