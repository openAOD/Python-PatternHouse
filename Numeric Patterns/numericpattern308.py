height = int(input())
x = 1

for i in range(1,height+1) :
    for j in range(1, height-i+1):
        print(end = "  ")
    
    for j in range(i, x+1):
        c = chr(j+64)
        print(c,end = " ")
        
    for j in range(i, x+1):
        print(j, end = " ")
        
    print()
    x = x+2
    
# Sample Input :- 5
# Output :-
#         A 1
#       B C 2 3
#     C D E 3 4 5
#   D E F G 4 5 6 7
# E F G H I 5 6 7 8 9
