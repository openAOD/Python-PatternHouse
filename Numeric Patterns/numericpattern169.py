height = int(input())

for i in range(1,height):

    for j in range(1,i*2):

        if(j < i):
            print(height+j-i,end=" ")

        elif(j == i):
            print(0,end=" ")

        else:
            print(height-j+i,end=" ")
            
    print()

# Sample Input :- 5
# Output :-
# 0 
# 4 0 4 
# 3 4 0 4 3 
# 2 3 4 0 4 3 2 
