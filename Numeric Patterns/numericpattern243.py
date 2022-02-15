height = int(input())
value = 1

for i in range(1, height + 1):

    for j in range(1,i+1):
    
        if(i == height or j == 1 or i == j):
            print(value,end=" ")
            value += 1
    
        else:
            print(end="   ")
        
    print()

# Sample Input :- 5
# Output :-
# 1 
# 2 3 
# 4    5 
# 6       7 
# 8 9 10 11 12 
