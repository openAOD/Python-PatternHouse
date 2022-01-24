def pypart2(n):
	k = 2*n - 2
	counter = 1
	for i in range(0, n):
	    for j in range(0, k):
	        print(end=" ")
	    k = k - 2
	    for j in range(0, i+1):
	        print((j+1)*(i+1), end=" ")
	        counter=counter+2
	    print("\r")

print("Enter the number of rows: ")
n = int(input())
pypart2(n)


Enter the number of rows: 
5
            1 
         2  4 
      3  6  9 
   4  8 12 16 
5 10 15 20 25 
