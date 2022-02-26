height = int(input())
k = height-1
x = 1
y = 1

for i in range(1,height+1):

    for j in range(1,k+1):
        print(end="  ")

    for j in range(1,i*2):

        if(i%2 != 0):
            print(x,end=" ")
            x += 1

            if(x >9):
                x = 1

        else:
            c = chr(y+64)
            print(c,end=" ")
            y += 1

    k -= 1
    print()

# Sample Input :- 5
# Output :-
#         1 
#       A B C 
#     2 3 4 5 6 
#   D E F G H I J 
# 7 8 9 1 2 3 4 5 6 
