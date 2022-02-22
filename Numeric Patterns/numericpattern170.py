height = int(input())
c = 1;

for i in range(1,height+1):
    p = 1

    for j in range(1,c+1):

        if(j%2 == 0):
            print("*",end=" ")

        else:
            print(p,end=" ")
            p += 1
    
    c += 2
    print()
    
# Sample Input :- 4
# Output :-
# 1 
# 1 * 2 
# 1 * 2 * 3 
# 1 * 2 * 3 * 4 
