height = int(input())

for i in range(0,height+1):

    for j in range(0,height-i+1):
        print(end=" ")

    for j in range(0,i):
        
        if(i%2 == 0):
            c = chr(j+65)
            print(c,end=" ")

        else:
            print(j+1,end=" ")
            
    print()
    
# Sample Input :- 5
# Output :-
#     1 
#    A B 
#   1 2 3 
#  A B C D 
# 1 2 3 4 5 
