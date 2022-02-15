height = int(input())

for i in range(1,height+1):

    for j in range(1,height+1):
    
        if(i == 1 and j != 1):
            n = height * 3 - j - 1
            print(n,end=" ")

        elif(j == 1):
            print(i,end=" ")

        elif(j == height - i + 1):
            n = (height*2) - height + j - 1
            print(n,end=" ")
            
        else:
            print(end="   ")
        
    print()
    
# Sample Input :- 5
# Output :- 
# 1 12 11 10 9 
# 2       8    
# 3    7       
# 4 6          
# 5             
