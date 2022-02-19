height = int(input()) 

for i in range(0,height):
    print(i,end=" ")

    for j in range(0,i):
        print("*",end=" ")

    print()
    
# Sample Input :- 6
# Output :-
# 0 
# 1 * 
# 2 * * 
# 3 * * * 
# 4 * * * * 
# 5 * * * * * 
