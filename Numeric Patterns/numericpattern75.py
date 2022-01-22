def pypart2(n):
	k = 2*n - 2
	counter = 0
	for i in range(0, n):
	    flag = 1
	    for j in range(0, k):
	        print(end=" ")
	        flag+=0.5
	    k = k - 2
	    flag = int(flag)
	    for j in range(0, i+1):
	        print(n-flag+1, end=" ")
	        flag=flag+1
	    counter=counter+1
	    print("\r")
	  
print("Enter the number of rows: ")
n = int(input())
pypart2(n)


# OUTPUT
# Enter the number of rows: 
# 5
#         1 
#       2 1 
#     3 2 1 
#   4 3 2 1 
# 5 4 3 2 1
