try:
    w = int(input("Number of chars in first line (default `5`): "))
    c = input("Enter the character for the pattern (default `*`): ")
except ValueError:
    print("!! Invalid input, defaults are being used !!")
    w = 5
    c = '*'


if len(c) == 0: c = '*'

def gen_pattern_164(w:int,char:str) -> str:
    s = [(char * i).rjust(w,' ') for i in range(w,0,-2)]
    s += s[-2::-1]
    return "\n".join(s)

print(gen_pattern_164(w,c))

"""
Number of chars in first line (default `5`): 5 
Enter the character for the pattern (default `*`): *
*****
  ***
    *
  ***
*****
"""