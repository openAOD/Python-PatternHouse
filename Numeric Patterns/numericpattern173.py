height = int(input())
x = 1
t = 1

for i in range(1,height):
    y = t

    for j in range(1,i+1):

        if(i%2 == 1):

            if(x <= 9):
                print("",x,end="# ")

            else:
                print(x,end="# ")

        else:
            if(y <= 9):
                print("",y,end="# ")

            else:
                print(y,end="# ")

        x += 1
        y -= 1
    
    t += i + 1;
    print()
            
# Sample Input :- 5
# Output :-
#  1# 
#  3#  2# 
#  4#  5#  6# 
# 10#  9#  8#  7# 
