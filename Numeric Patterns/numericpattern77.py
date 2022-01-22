def pypart2(n):
	k = 2*n - 2
	counter = 1
	for i in range(0, n):
	    for j in range(0, k):
	        print(end=" ")
	    k = k - 2
	    for j in range(0, i+1):
	        print(counter, end=" ")
	        counter=counter+2
	    print("\r")
	  
print("Enter the number of rows: ")
n = int(input())
pypart2(n)

OUTPUT

# Enter the number of rows: 
# 5
#              1 
#            3 5 
#         7 9 11 
#    13 15 17 19 
# 21 23 25 27 29 
