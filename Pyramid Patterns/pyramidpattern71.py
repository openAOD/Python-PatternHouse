height = int(input())

for i in range(0,height+1):

    for j in range(0,i):
        print(end=" ")

    for j in range(height,i,-1):
        
        if(i%2 == 0):
            c = chr(height-i+64)
            print(c,end=" ")

        else:
            print(height-i,end=" ")
            
    print()
    
# Sample Input :- 5
# Output :-
# E E E E E 
#  4 4 4 4 
#   C C C 
#    2 2 
#     A 
     
