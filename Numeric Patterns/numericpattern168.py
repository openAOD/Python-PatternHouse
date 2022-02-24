height = int(input())

for i in range(1,height+1):

    for j in range(1,i*2):

        if(j <= i):
            print(i-j+1,end=" ")

        else:
            print(j-i+1,end=" ")
            
    print()

# Sample Input :- 4
# Output :-
# 1 
# 2 1 2 
# 3 2 1 2 3 
# 4 3 2 1 2 3 4 
