"""
In this question, we have to print stars from 1 to n
We can use a for loop starting from 1 (because we start with 1 star) which goes till n+1 (because upper limit is ignored)
"""
n = 5 # size
for i in range(1, n+1):
    print("*"*i)

"""
OUTPUT:

*
**
***
****
*****
"""