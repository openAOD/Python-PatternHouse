def pypart2(n):
	alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	k = 2*n - 2
	flag = n-1
	for i in range(0, n):
		for j in range(0, k):
			print(end=" ")
		k = k - 2
		for j in range(0, i+1):
		    if(i%2==0):
		        print(alpha[i], end=" ")
		    else:
		        print(i+1,end=" ")
		print("\r");
		
		
print("Enter the number of rows: ")
n = int(input())
pypart2(n)
