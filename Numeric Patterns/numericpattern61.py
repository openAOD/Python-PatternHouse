height = int(input())
c = 1

for i in range(height,0,-1) :

    for j in range(1, i+1):

        if(c <= 9):
            print("",c,end = " ")
        else:
            print(c,end = " ")
            
        c += 1
        
    print()

// Sample Input :- 5
// Output :-
//  1  2  3  4  5
//  6  7  8  9
// 10 11 12
// 13 14
// 15

