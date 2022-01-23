height = int(input())

for i in range(1,height+1):

    for j in range(1,height-i+1):
    
        print(end="  ")
        
    for j in range(1,i+1):
    
        if(i%2 == 0):
            print(j,end=" ")
        
        else:
            c = chr(j+64)
            print(c,end=" ")
    print()
    
# Sample Input :- 5
# Output :-
#         A
#       1 2
#     A B C
#   1 2 3 4
# A B C D E
