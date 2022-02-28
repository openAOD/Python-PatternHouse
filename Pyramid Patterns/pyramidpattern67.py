height = int(input())

for i in range(0,height+1):

    for j in range(0,height-i+1):
        print(end=" ")

    for j in range(0,i):
        
        if(i%2 == 0):
            print(i,end=" ")

        else:
            c = chr(i+64)
            print(c,end=" ")
            
    print()
    
# Sample Input :- 5
# Output :-       
#      A 
#     2 2 
#    C C C 
#   4 4 4 4 
#  E E E E E 
