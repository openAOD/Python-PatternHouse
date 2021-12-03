n = 4
for i in range(n+1):
    print(" "*(2*(n-i))+"* "*i)
for i in range(n-1, 0, -1):
    print(" "*(2*(n-i))+"* "*i)

"""
OUTPUT:

      * 
    * *
  * * *
* * * *
  * * *
    * *
      *
"""