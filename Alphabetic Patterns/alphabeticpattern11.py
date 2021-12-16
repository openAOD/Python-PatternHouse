# Left triangle pattern
n = 5
for i in range(n):
    for j in range(i+1):
        print(chr(69-j), end="")
    print()

'''

Output:
E
ED
EDC
EDCB
EDCBA

'''
