height = int(input())

for i in range(1,height+1):

    for j in range(1,height*2+1):
        if(j == height-i+1 or j == height+i-1):
            c = chr(j+64)
            print(c,end=" ")

        else:
            print(end="  ")

    print()

# Sample Input :- 5
# Output :-
#         E           
#       D   F         
#     C       G       
#   B           H     
# A               I   
