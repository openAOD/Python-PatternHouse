height = int(input())

for i in range(0,height):

    for j in range(0,height):
    
        if(i == 0 or i == height//2 or i == height-1):
            print("5",end=" ")
        elif(i < height//2 and j == 0):
            print("5",end=" ")
        elif(i > height//2 and j == height-1):
            print("5",end=" ")
        else:
            print(end="  ")
    print()
    
# Sample Input :- 5
# Output :-
# 5 5 5 5 5
# 5
# 5 5 5 5 5
#         5
# 5 5 5 5 5 
