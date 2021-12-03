n = 5
for rows in range(n, 0, -1):
    for columns in range(0, n-rows): 
        print(end=" ") # printing space and staying in same line
    for columns in range(0, rows):
        print("*", end=" ") # printing * and staying in same line
    print() # printing new line

"""
OUTPUT:

* * * * * 
 * * * * 
  * * *
   * *
    *
"""