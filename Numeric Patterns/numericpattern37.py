height = int(input())

for i in range(1,height+1) :

    for j in range(1, i+1):
        
        m = i*j
        if(m <= 9):
            print("",m,end = " ")
        else:
            print(m,end = " ")
        
    print()

# Sample Input :- 5
# Output :-
#  1
#  2  4
#  3  6  9
#  4  8 12 16
#  5 10 15 20 25 

