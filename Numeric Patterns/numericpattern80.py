def pypart2(n):
	k = 2*n - 2
	counter = 1
	for i in range(0, n):
	    for j in range(0, k):
	        print(end=" ")
	    k = k - 2
	    for j in range(0, i+1):
	        print(counter*counter, end=" ")
	        counter=counter+1
	    print("\r")

print("Enter the number of rows: ")
n = int(input())
pypart2(n)


#OUTPUT

# Enter the number of rows: 
# 5
#                   1  
#               4   9 
#          16  25  36 
#      49  64  81 100 
# 121 144 169 196 225 
