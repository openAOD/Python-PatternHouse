height = int(input())

for i in range(1,height+1):

    for j in range(1,height-i+1):
        print(end="  ")

    for j in range(1,i+1):
        print(i,end=" ")

    for j in range(1,i+1):
        ch = chr(i+64)
        print(ch,end=" ")

    print()

# Sample Input :- 5
# Output :-
#         1 A 
#       2 2 B B 
#     3 3 3 C C C 
#   4 4 4 4 D D D D 
# 5 5 5 5 5 E E E E E 
