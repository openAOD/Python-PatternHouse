def pypart2(n):
	alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	k = 2*n - 2
	flag = n-1
	for i in range(0, n):
		for j in range(0, k):
			print(end=" ")
		k = k - 2
		counter = flag
		for j in range(0, i+1):
			print(alpha[counter], end=" ")
		flag = flag -1
		print("\r")
		
		
print("Enter the number of rows: ")
n = int(input())
pypart2(n)



# OUTPUT

# Enter the number of rows: 
# 5
#         E 
#       D D 
#     C C C 
#   B B B B 
# A A A A A 
