height = int(input())

for i in range(1,height+1):

    for j in range(1,height-i+1):
    
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
#     1
#    B B
#   3 3 3
#  D D D D
# 5 5 5 5 5
