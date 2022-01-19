height = int(input())
m = height

for i in range(1,height+1) :

    for j in range(1, i+1):
        print(m,end = " ")
    m-=1
        
    print()

// Sample Input :- 5
// Output :-
// 5
// 4 4
// 3 3 3 
// 2 2 2 2
// 1 1 1 1 1
