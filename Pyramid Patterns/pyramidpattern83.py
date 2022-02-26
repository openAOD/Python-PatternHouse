height = int(input())
c = 1;

for i in range(1,height+1):

    for j in range(1,height-i+1):
        print(end="  ")

    for j in range(i,c+1):
        print(j,end=" ")

    for j in range(i,c+1):
        ch = chr(j+64)
        print(ch,end=" ")

    c += 2
    print()

# Sample Input :- 5
# Output :-
#         1 A 
#       2 3 B C 
#     3 4 5 C D E 
#   4 5 6 7 D E F G 
# 5 6 7 8 9 E F G H I 
