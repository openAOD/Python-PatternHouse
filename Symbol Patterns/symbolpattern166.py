height = int(input())

for i in range(height//2,height+1,2):
    for j in range(1,height-i,2):
        print(end="  ")

    for j in range(1,i+1):
        print("*",end=" ")
        
    for j in range(1,height-i+1):
        print(end="  ")

    for j in range(1,i+1):
        print("*",end=" ")

    print()

for i in range(height,0,-1):
    for j in range(i,height):
        print(end="  ")

    for j in range(0,i*2-1):
        print("*",end=" ")

    print()
    
# Sample Input :- 5
# Output :-
#   * *       * *  
# * * * *   * * * * 
# * * * * * * * * * 
#   * * * * * * *  
#     * * * * * 
#       * * *
#         *
