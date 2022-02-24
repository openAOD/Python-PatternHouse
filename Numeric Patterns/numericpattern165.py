
height = int(input())
c = 1
c1 = 1

for i in range(1,height+1):
    
    for j in range(1,i+1):
        
        if(i%2 == 0):
            ch = chr(c1+64)
            print(ch,end=" ")
            c1 += 1

        else:
            print(c,end=" ")
            c += 1

    print()
    
# Sample Input :- 5
# Output :-
# 1 
# A B 
# 2 3 4 
# C D E F 
# 5 6 7 8 9 
