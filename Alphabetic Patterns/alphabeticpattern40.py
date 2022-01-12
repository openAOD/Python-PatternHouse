alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def pattern(n):
    count = 0
    for i in range(n):
        for j in range(n - i - 1):
            print(' ', end='')
        flag = count
        wflag = 1
        caser = 1
        for k in range(2 * i + 1):
            print(alpha[flag], end='')
            if(flag == 0):
                caser = 0
                wflag = 0
            if(caser!=0 and wflag!=0):
                flag = flag - 1
            if(caser == 0):
                flag = flag + 1
        print()
        count = count + 1


print("Enter the number of rows: ")
n = int(input())
pattern(n)
