height = int(input()) 

for i in range(height,0,-1):

    for j in range(i,height):
        print(end=" ")

    for j in range(1,i+1):

        if(i%2 == 0):
            c = chr(i+64)
            print(c,end=" ")

        else:
            print(i,end=" ")

    print()
    
# Sample Input :- 5
# Output :-
# 5 5 5 5 5 
#  D D D D 
#   3 3 3 
#    B B 
#     1 
