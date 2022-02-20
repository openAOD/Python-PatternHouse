height = int(input()) 
x = 1
n = 1

for i in range(0,height):

    for j in range(height-1,i,-1):
        print(end="  ")

    for j in range(0,i*2-1):

        if(i%2 == 0):
            c = chr(x+64)
            print(c,end=" ")
            x += 1

        else:
            print(n,end=" ")
            n += 1
            if(n > 9) :
                n = 1

    print()
    
# Sample Input :- 6
# Output :-
#         1 
#       A B C 
#     2 3 4 5 6 
#   D E F G H I J 
# 7 8 9 1 2 3 4 5 6 
