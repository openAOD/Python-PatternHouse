height = int(input()) 

for i in range(0,height):

    for j in range(i,height):
        print(end="  ")

    for j in range(1,i+1):

        if(i%2 == 0):
            print(j,end=" ")

        else:
            c = chr(j+64)
            print(c,end=" ")
                                    
    print()
    
# Sample Input :- 6
# Output :-
#          A 
#        1 2 
#      A B C 
#    1 2 3 4 
#  A B C D E 