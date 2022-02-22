height = int(input())

for i in range(1,height+1):
    c = 1

    for j in range(1,i*2):
        print(c,end=" ")
        c += 1
           
    print()

# Sample Input :- 4
# Output :-
# 1 
# 1 2 3 
# 1 2 3 4 5 
# 1 2 3 4 5 6 7 
