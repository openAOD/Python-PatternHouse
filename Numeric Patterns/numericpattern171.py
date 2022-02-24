height = int(input())
x = 1

for i in range(1,height):

    for j in range(1,i+1):

        print(x,end="# ")
        x += 1
    
    print()
            
# Sample Input :- 5
# Output :-
# 1# 
# 2# 3# 
# 4# 5# 6# 
# 7# 8# 9# 10# 
