height = int(input()) 

for i in range(height,0,-1):

    for j in range(1,i+1):

        if(i%2 == 0):
            print(j,end=" ")
            
        else:
            c = chr(j+64)
            print(c,end=" ")

    print()

# Sample Input :- 5
# Output :-
# A B C D E 
# 1 2 3 4 
# A B C 
# 1 2 
# A 
