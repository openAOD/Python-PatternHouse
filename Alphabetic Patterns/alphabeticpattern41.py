rows=int(input("Number of rows = "))
ch = 'A'

for i in range (1,rows+1):
    for space in range(rows-i):
        print(' ',end='')

    for j in range(1, i+1):
        print(ch,end="")
        ch=ord(ch)+1
        ch = chr(ch)
    ch=ord(ch)-1
    ch = chr(ch)

    for k in range(1, i):
        ch=ord(ch)-1
        ch = chr(ch)
        print(ch,end="")


    print()
    ch='A' 