height = int(input())

for i in range(1,height+1):
   
    for j in range(1,height+1):

        if(i == height//2+1 or j == height//2+1):
            print("*",end=" ")

        else :
            print(end="  ")

    print()
    
# Sample Input :- 5
# Output :-
#     *
#     *
# * * * * *
#     *
#     *
