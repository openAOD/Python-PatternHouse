def pypart2(n):
	k = 2*n - 2
	counter = 1
	flag=n
	for i in range(0, n):
	    for j in range(0, k):
	        print(end=" ")
	    k = k - 2
	    for j in range(0, i+1):
	        print(counter-j, end=" ")
	    counter=counter+flag
	    flag = flag-1
	    print("\r")

print("Enter the number of rows: ")
n = int(input())
pypart2(n)


#OUTPUT
# Enter the number of rows: 
# 5
#         1 
#       6 2
#     10 7 3 
#   13 11 8 4 
# 15 14 12 10 9
