height = int(input())

for i in range(1, height + 1):
    value = 3 * height - i - 1

    for j in range(1,i+1):
    
        if(i == height):
            print(height + j - 1,end=" ")

        elif(j == 1):
            print(i,end=" ")

        elif(j == i):
            print(value,end=" ")
            
        else:
            print(end="  ")
        
    print()

# Sample Input :- 5
# Output :-
# 1 
# 2 12 
# 3   11 
# 4     10 
# 5 6 7 8 9 
