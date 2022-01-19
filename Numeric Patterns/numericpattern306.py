height = int(input())

for i in range(1,height+1) :
    for j in range(1, height-i+1):
        print(end = "  ")
    
    for j in range(1, i+1):
        c = chr(i+64)
        print(c,end = " ")
        
    for j in range(1, +1):
        print(i,end = " ")
        
    print()
    
# Sample Input :- 5
# Output :-
#          A 1
#        B B 2 2
#      C C C 3 3 3
#    D D D D 4 4 4 4
#  E E E E E 5 5 5 5 5 
