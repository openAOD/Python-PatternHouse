"""
In this question, we have to print stars from n to 0 along with spaces before n-1 stars
We can use a for loop starting from n which goes till 0 and has -1 as the step
Since the upper limit is ignored, the loop will end on 1 star
To print the spaces, we have to print n-i (i being the variable in the for loop) spaces (if n is 5 and i is 4, then we print 5-4 = 1 spaces) and then the star i times
"""
n = 5 # size
for i in range(5, 0, -1):
    print(" "*(n-i)+"*"*i)

"""
OUTPUT:

*****
 ****
  ***
   **
    *
"""