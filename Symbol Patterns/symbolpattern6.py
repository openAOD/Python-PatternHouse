n = 5 # size
for rows in range(n):
    for columns in range(-n, -rows-1):
        print(" ", end="") # printing space and staying in same line
    for columns in range(rows+1):
        print("* ", end="") # printing * and staying in same line
    print() # printing new line

"""
OUTPUT:

    * 
   * * 
  * * *
 * * * *
* * * * *
"""