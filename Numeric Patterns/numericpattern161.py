height = int(input())
x = 1

for i in range(0,height):

    for j in range(0, height):

        if((i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)) :
            print(" *",end=" ")

        else :
            if(x <= 9):
                print("",x,end=" ")

            else:
                print(x,end=" ")
            x += 1

    print()
    
# Sample Input :- 5
# Output :-
# *  1  *  2  * 
# 3  *  4  *  5 
# *  6  *  7  * 
# 8  *  9  * 10 
# * 11  * 12  * 
