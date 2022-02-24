height = int(input())
x = 0

for i in range(1,height+1):

    for j in range(1,i*2):

        if(j <= i):
            print(j+x,end=" ")

        else:
            print(i*2-j+x,end=" ")

    x += i        
    print()

# Sample Input :- 4
# Output :-
# 1 
# 2 3 2 
# 4 5 6 5 4 
# 7 8 9 10 9 8 7 
