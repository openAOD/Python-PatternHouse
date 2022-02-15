height = int(input())
num = 1

for i in range(1, height + 1):

    for j in range(1, height - i + 2):

        if(i == 1 or j == 1 or j == height - i + 1):

            if(num <= 9):
                print("",num,end=" ")

            else :
                print(num,end=" ")

            num += 1

        else:
            print(end="   ")

    print()

# Sample Input :- 5
# Output :- 
#  1  2  3  4  5 
#  6        7 
#  8     9 
# 10 11 
# 12 
