n = int(input("Width: "))

def gen180(n:int):
    A = ['*'*n]
    A.extend([f'*{" "*(n-2)}*' for i in range(1,n//2)])
    A.append(A[0])
    A.extend([f'{" "*(n-1)}*' for i in range(1,n//2)])
    A.append(A[0])
    return "\n".join(A)
    
print(gen180(n))

"""
Width: 5
*****
*   *
*****
    *
*****
"""