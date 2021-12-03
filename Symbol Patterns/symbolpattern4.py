"""
In this question, we have to print stars from 1 to n along with spaces before them except at the end
We can use a for loop starting from 1 (because we start with 1 star) which goes till n+1 (because upper limit is ignored)
To print the spaces, we have to print n-i (i being the variable in the for loop) spaces (if n is 5 and i is 1, then we print 5-1= 4 spaces) and then the star i times
"""
n = 5 # size
for i in range(1, n+1):
    print(" "*(n-i)+"*"*i)

"""
OUTPUT:

    *
   **
  ***
 ****
*****
"""