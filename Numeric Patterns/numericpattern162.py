
height = int(input())

for i in range(1,height+1):

    for j in range(1,2*height):
    
        if(i == j or j == height or j == 2*height-i):
            print("*",end=" ")

        else:
            print(0,end=" ")
            
    print()

# Sample Input :- 4
# Output :-
# * 0 0 * 0 0 * 
# 0 * 0 * 0 * 0 
# 0 0 * * * 0 0 
# 0 0 0 * 0 0 0 
