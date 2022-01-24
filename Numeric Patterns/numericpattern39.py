def pypart2(n):
	counter = 1
	flag=n-1
	for i in range(0, n):
	    for j in range(0, i+1):
	        print(counter-j, end=" ")
	    counter=counter+flag
	    flag = flag-1
	    print("\r")

print("Enter the number of rows: ")
n = int(input())
pypart2(n)
