height = int(input())

for i in range(1,height+1):

    for j in range(1,height-i+1):
    
        print(end=" ")
    
    for j in range(1,i+1):
    
        if((i+j)%2 != 0):
            print("*",end=" ")
        
        else:
            print("#",end=" ")
            
    print()
    
# Sample Input :- 5
# Output :-
#     #
#    * #
#   # * #
#  * # * #
# # * # * #
