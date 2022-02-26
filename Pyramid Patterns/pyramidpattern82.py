height = int(input())

for i in range(1,height+1):

    for j in range(1,height-i+1):
        print(end="  ")

    for j in range(1,i+1):
        print(j,end=" ")

    for j in range(1,i+1):
        ch = chr(j+64)
        print(ch,end=" ")

    print()

# Sample Input :- 5
# Output :-
#         1 A 
#       1 2 A B 
#     1 2 3 A B C 
#   1 2 3 4 A B C D 
# 1 2 3 4 5 A B C D E 
