def triangle(n):
	k = n - 1
	for i in range(0, n):
		for j in range(0, k):
			print(end=" ")
		k = k - 1
		for j in range(0, i+1):
			if(i%2!=0):
			    print("* ", end="")
			else:
			    print("# ", end="")
		print("\r")
		
		
print("Enter the number of rows: ")
n = int(input())
triangle(n)


#OUTPUT

# Enter the number of rows: 
# 5
#      # 
#     * * 
#    # # # 
#   * * * * 
#  # # # # # 
