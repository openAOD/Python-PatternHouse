height = int(input()) 

for i in range(0,height):

    for j in range(i,height):
        print(end=" ")

    for j in range(1,i+1):

        if(i%2 == 0):
            print(i,end=" ")

        else:
            c = chr(i+64)
            print(c,end=" ")
            
    print()
    
# Sample Input :- 6
# Output :-
#      A 
#     2 2 
#    C C C 
#   4 4 4 4 
#  E E E E E 
