height = int(input())

for i in range(0,height) :

    for j in range(0, height):
    
        if(j%2 != 0):
            print(1,end = " ")
        else:
            print(0, end=" ")
        
    print()
    
// Sample Input :- 5
// Output :-
// 0 1 0 1 0
// 0 1 0 1 0
// 0 1 0 1 0
// 0 1 0 1 0
// 0 1 0 1 0
