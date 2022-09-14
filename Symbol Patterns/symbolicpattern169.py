n=max=5
symbol_arr=[4,3,5,1,2]
for i in range(max):
    for j in range(n):
        if symbol_arr[j] >= max-i:
            print(' # ',end='')
        else:
            print('   ', end='')
    print(end='\n')
for i in range(n):
    print([i+1],end='')