n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):
        print(chr(k+65), end='')
    print()

'''

Output:
    
    A
   ABC
  ABCDE
 ABCDEFG
ABCDEFGHI
 
'''
