height = int(input())

for i in range(1,height+1):

    for j in range(1,height-i+1):
    
        print(end=" ")
        
    for j in range(1,i+1):
    
        if(i%2 == 0):  
            c = chr(j+64)
            print(c,end=" ")
            
        else:
            print(j,end=" ")
            
    print()
    
# Sample Input :- 5
# Output :-
#     1
#    A B
#   1 2 3
#  A B C D
# 1 2 3 4 5
