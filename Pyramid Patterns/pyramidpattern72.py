height = int(input())

for i in range(0,height+1):

    for j in range(0,i):
        print(end=" ")

    for j in range(height,i,-1):
        
        if(i%2 == 0):
            c = chr(height-j+65)
            print(c,end=" ")

        else:
            print(height-j+1,end=" ")
            
    print()
    
# Sample Input :- 5
# Output :-
# A B C D E 
#  1 2 3 4 
#   A B C 
#    1 2 
#     A 
     
