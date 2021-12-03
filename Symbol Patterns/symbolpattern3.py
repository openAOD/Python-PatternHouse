"""
In this question, we have to print stars from n to 0
We can use a reversed for loop starting from n which goes till 0 and has -1 as the step
Since the upper limit is ignored, the loop will end on 1 star
"""
n = 5 # size
for i in range(n, 0, -1):
    print("*"*i)

"""
OUTPUT:

*****
****
***
**
*
"""