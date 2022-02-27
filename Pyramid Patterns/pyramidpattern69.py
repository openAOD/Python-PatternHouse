height = int(input())

for i in range(0,height+1):

    for j in range(0,height-i+1):
        print(end=" ")

    for j in range(0,i):
        
        if(i%2 == 0):
            c = chr(i+64)
            print(c,end=" ")

        else:
            print(i,end=" ")
            
    print()
    
# Sample Input :- 5
# Output :-
#      1 
#     B B 
#    3 3 3 
#   D D D D 
#  5 5 5 5 5 
