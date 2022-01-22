def pypart2(n):
	k = 2*n - 2
	counter = 0
	for i in range(0, n):
		for j in range(0, k):
			print(end=" ")
		k = k - 2
		
		for j in range(0, i+1):
			print(j+1, end=" ")
		counter=counter+1
		print("\r")
		
		
print("Enter the number of rows: ")
n = int(input())
pypart2(n)

OUTPUT
# Enter the number of rows: 
# 5
#         1 
#       1 2 
#     1 2 3 
#   1 2 3 4 
# 1 2 3 4 5
