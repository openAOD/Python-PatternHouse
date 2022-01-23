height = int(input())

for i in range(1, height+1):

    for j in range(1,height+1):
    
        if(i == j or i == height-j+1):
            c = chr(j + 64)
            print(c,end=" ")
        
        else:
            print(end = "  ")
            
    print()
    
# Sample Input :- 5
# Output :- 
# A       E
#   B   D
#     C
#   B   D
# A       E
