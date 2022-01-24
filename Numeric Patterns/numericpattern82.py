def pypart2(n):
	k = 2*n - 2
	counter = 15
	for i in range(0, n):
	    for j in range(0, k):
	        print(end=" ")
	    k = k - 2
	    for j in range(0, i+1):
	        print(counter, end=" ")
	        counter=counter-1
	    print("\r")

print("Enter the number of rows: ")
n = int(input())
pypart2(n)

#OUTPUT

# Enter the number of rows: 
# 5
#           15 
#        14 13 
#     12 11 10 
#   9  8  7  6 
# 5 4  3  2  1 
