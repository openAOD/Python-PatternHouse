height = int(input())

for i in range(1,height+1):

    for j in range(1,height*2+1):
        if(j == i or j == 2*height-i):
            c = chr(height-i+65)
            print(c,end=" ")

        else:
            print(end="  ")

    print()

# Sample Input :- 5
# Output :-
# E               E   
#   D           D     
#     C       C       
#       B   B         
#         A        
