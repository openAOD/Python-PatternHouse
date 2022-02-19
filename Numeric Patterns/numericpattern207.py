height = int(input()) 

for i in range(0,height):

    for j in range(i,height):
        print(end="  ")

    for j in range(1,i+1):

        if(i%2 == 0):
            c = chr(i+64)
            print(c,end=" ")

        else:
            print(i,end=" ")
                        
    print()
    
# Sample Input :- 6 
# Output :-
#           1 
#         B B 
#       3 3 3 
#     D D D D 
#   5 5 5 5 5 
