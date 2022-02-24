
height = int(input())

for i in range(1,height+1):
    c = 1

    for j in range(1,i+1):
    
        if(i%2 == 0):
            print(j*2,end=" ")

        else:
            print(c,end=" ")
            c += 2
            
    print()

# Sample Input :- 5
# Output :-
# 1 
# 2 4 
# 1 3 5 
# 2 4 6 8 
# 1 3 5 7 9 
