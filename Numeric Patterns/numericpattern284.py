height = int(input())
x = 1

for i in range(1,height+1):

    for j in range(1,2*x):

        if(i <= height//2+1 and j%2 == 1):
            print(i,end=" ")

        elif(i > height//2+1 and j%2 == 1):
            print(height-i+1,end=" ")
        
        else:
            print("*",end=" ")

    if(i <= height//2):
        x += 1
    
    else :
        x -= 1

    print()
    
# Sample Input :- 7
# Output :-
# 1 
# 2 * 2 
# 3 * 3 * 3 
# 4 * 4 * 4 * 4 
# 3 * 3 * 3 
# 2 * 2 
# 1 
