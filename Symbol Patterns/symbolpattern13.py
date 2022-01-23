[13:04, 23/01/2022] Mahak Garg: height = int(input())

for i in range(1, height+1):

    for j in range(1,i+1):
    
        print(j,end=" ")
        
    for j in range(1, height-i+1):
        print("*",end=" ")
        
    print()
    
# Sample Input :- 5
# Output :-
# 1 * * * *
# 1 2 * * * 
# 1 2 3 * * 
# 1 2 3 4 *
# 1 2 3 4 5
