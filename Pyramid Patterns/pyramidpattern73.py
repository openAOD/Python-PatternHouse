height = int(input())

for i in range(0,height+1):

    for j in range(0,i):
        print(end=" ")

    for j in range(height,i,-1):
        
        if(i%2 == 0):
            print(height-i,end=" ")

        else:
            c = chr(height-i+64)
            print(c,end=" ")

    print()
    
# Sample Input :- 5
# Output :-
# 5 5 5 5 5 
#  D D D D 
#   3 3 3 
#    B B 
#     1 
     
