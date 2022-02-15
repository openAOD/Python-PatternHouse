height = int(input())

for i in range(1, height + 1):

    for j in range(1, height + 1):

        if(j == height - i + 1):
            num = height - i
            print(num,end=" ")

        elif(j < height - i + 1):
            print("*",end=" ")

        else:
            print(end="  ")

    print()

# Sample Input :- 6
# Output :-
# * * * * * 5 
# * * * * 4   
# * * * 3     
# * * 2       
# * 1         
# 0           
