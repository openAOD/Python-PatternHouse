height = int(input())
c = 1
k = 1
c1 = 0

for i in range(1, height+1):

    for j in range(1,height-i+1):
    
        print(end="  ")
        
    for j in range(1,k+1):
    
        if(i%2 == 0):  
            ch = chr(c1 + 65)
            print(ch,end=" ")
            c1 += 1
            
        else:
            print(c,end=" ")
            c += 1
            
        if(c > 9):
            c = 1
            
    k = k + 2       
    print()
    
# Sample Input :- 5
# Output :-
#         1
#       A B C
#     2 3 4 5 6
#   D E F G H I J
# 7 8 9 1 2 3 4 5 6
